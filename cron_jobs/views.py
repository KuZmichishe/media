# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.conf import settings
import helper as Cron
from films.models import Film, Genre
from datetime import datetime


def index(request):
    for item in Cron.files_to_array(settings.DOWNLOADS_ROOT):
        if item['type'] == 'movie':
            film = Film(
                title=item['title'],
                overview=item['overview'],
                genre=Genre.objects.get(pk=item['genre']),
                background=item['background'],
                poster=item['poster'],
                file_name=item['file_name'],
                file_extension=item['file_extension'],
                file_size=item['file_size'],
                #first_air_date=datetime.strptime(item['first_air_date'], '%Y-%m-%d'),
                movie_db_id=item['movie_db_id'],
            )
            film.save()

    return JsonResponse({
        'success': Cron.files_to_array(settings.DOWNLOADS_ROOT)
    })
