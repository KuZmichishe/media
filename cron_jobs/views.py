# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.conf import settings
import helper as Cron
from films.models import Film, Genre
from datetime import datetime
import os


def register_files(request):
    for item in Cron.files_to_array(settings.DOWNLOADS_ROOT):
        if item['type'] == 'movie':
            film = Film(
                title=item['title'],
                file_name=item['file_name'],
                file_extension=item['file_extension'],
                file_size=item['file_size'],
            )
            try:
                film.save()
                os.rename(
                    settings.DOWNLOADS_ROOT + item['file_name'],
                    settings.FILMS_ROOT + item['file_name']
                )
            except Exception as e:
                print e
    return JsonResponse({
        'success': True
    })


def update_video_data(request):
    films = Film.objects.filter(is_updated=0)
    for film in films:
        movie_data = Cron.get_movie_data(film.title, 'movie')
        if movie_data:
            info = movie_data[0]
            film.background = info['backdrop_path']
            film.poster = info['poster_path']
            film.movie_db_id = info['id']
            film.overview = info['overview']
            film.genre = Genre.objects.get(pk=info['genre_ids'][0])
            film.first_air_date = info['release_date']
        film.is_updated = True
        film.save()
    return JsonResponse({'sucess': movie_data})