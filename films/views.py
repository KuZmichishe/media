# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Film, Genre


def index(request):
    films = Film.objects.all()
    return render(request, 'films/index.html')
