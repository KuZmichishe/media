from django.conf import settings
from django.core.files import File
from django.http import JsonResponse

import os
import os.path
import PTN
import requests
import json

def files_to_array(dirpath):
    filesList = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(tuple(settings.MEDIA_EXTENSIONS))]:
            f = open(os.path.join(dirpath, filename))
            myfile = File(f)
            info = PTN.parse(filename)
            if 'episode' in info.keys():
                type = 'tv'
            else:
                type = 'movie'
            filesList.append({
                'size': sizify(myfile.size),
                'name': os.path.join(dirpath, filename),
                'info': get_movie_data(info['title'], type)
            })
    return filesList

def sizify(value):
    if value < 512000:
        value = value / 1024.0
        ext = 'kb'
    elif value < 1073741824:
        value = value / 1048576.0
        ext = 'mb'
    else:
        value = value / 1073741824.0
        ext = 'gb'
    return '%s %s' % (str(round(value, 2)), ext)


def get_movie_data(video_title, type):
    domain = 'https://api.themoviedb.org/3/search/'
    url = domain + type + '?api_key=' + settings.MOVIEDB_API_KEY + '&language=' + settings.LANGUAGE_CODE + '&page=1&include_adult=true&query=' + video_title
    response = json.loads(requests.request("GET", url).text)['results']
    return response
