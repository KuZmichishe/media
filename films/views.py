# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Film
from django.conf import settings
from django.utils.encoding import smart_str
from django.http import HttpResponse


def index(request):
    films = Film.objects.all()
    poster_domain = settings.MOVIEDB_IMAGE_PATH + settings.MOVIEDB_POSTER_SIZE
    return render(
        request,
        'films/index.html',
        {
            'films': films,
            'poster_domain': poster_domain,
            'no_image': settings.NO_IMAGE_FAKE
        }
    )


def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    poster_domain = settings.MOVIEDB_IMAGE_PATH + settings.MOVIEDB_POSTER_SIZE
    background_domain = settings.MOVIEDB_IMAGE_PATH + settings.MOVIEDB_BACKGROUND_SIZE
    return render(
        request,
        'films/detail.html',
        {
            'film': film,
            'poster_domain': poster_domain,
            'background_domain': background_domain,
        })


def download_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    path_to_file = settings.FILMS_ROOT + film.file_name

    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(film.file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response
