from media.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    'media.kuzmich.xyz'
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'media',
        'USER': 'root',
        'PASSWORD': 'KIds528yes',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = '/mnt/Files/'
DOWNLOADS_ROOT = MEDIA_ROOT + 'downloads/'
FILMS_ROOT = MEDIA_ROOT + 'Video/Films/'
SHOWS_ROOT = MEDIA_ROOT + 'Video/Serials/'
