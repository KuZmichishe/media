from django.conf import settings

import os
import os.path
import PTN
import requests


def files_to_array(dirpath):
    filesList = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(tuple(settings.MEDIA_EXTENSIONS))]:
            info = PTN.parse(filename)

            if 'episode' in info.keys():
                type = 'tv'
            else:
                type = 'movie'
                filesList.append({
                    'title': info['title'],
                    'file_name': filename,
                    'file_extension': info['container'],
                    'file_size': sizify(os.path.getsize(os.path.join(dirpath, filename))),
                    'type': type,
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
    url = settings.MOVIEDB_DOMAIN + type + '?api_key=' + settings.MOVIEDB_API_KEY + '&language=' + settings.LANGUAGE_CODE + '&page=1&include_adult=true&query=' + video_title
    return requests.request("GET", url).json()['results']
