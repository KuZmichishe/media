from media.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

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

INSTALLED_APPS += (
    'django_cron',
)

MEDIA_ROOT = 'multimedia/'
DOWNLOADS_ROOT = MEDIA_ROOT + 'downloads/'
FILMS_ROOT = MEDIA_ROOT + 'films/'
SHOWS_ROOT = MEDIA_ROOT + 'shows/'
