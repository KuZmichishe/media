# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.conf import settings
import helper as Cron

def index(request):
    
    return JsonResponse({'success': Cron.files_to_array(settings.DOWNLOADS_ROOT)})