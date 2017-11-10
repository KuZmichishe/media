# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Show
from django.http import JsonResponse


def index(request):
    return JsonResponse({
        'success': True
    })


def show_detail(request, show_id):
    return JsonResponse({
        'success': True
    })


def season_detail(request, show_id, season_id):
    return JsonResponse({
        'success': True
    })
