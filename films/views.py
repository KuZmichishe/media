# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Film, Genre


def index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html', {'films': films})


def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'films/detail.html', {'film': film})