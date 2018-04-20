# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Film
from django.conf import settings
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    films_list = Film.objects.all()
    poster_domain = settings.MOVIEDB_IMAGE_PATH + settings.MOVIEDB_POSTER_SIZE

    paginator = Paginator(films_list, settings.LIST_LIMIT)
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    films = paginator.page(page)
    r = range(1, films.paginator.num_pages+1)

    return render(
        request,
        'films/index.html',
        {
            'films': films,
            'range': r,
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


def edit(request, film_id):
    film = get_object_or_404(Film, pk=film_id)


def download_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    path_to_file = settings.FILMS_ROOT + film.file_name

    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(film.file_name)
    response['X-Sendfile'] = path_to_file + smart_str(film.file_name)
    return response
