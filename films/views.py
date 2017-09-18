# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Film
from django.conf import settings


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
