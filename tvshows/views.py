# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return JsonResponse({
        'success': False
    })


def show_detail(request):
    return JsonResponse({
        'success': True
    })


def season_detail(request):
    return JsonResponse({
        'success': True
    })
