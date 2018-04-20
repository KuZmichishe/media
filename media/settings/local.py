from media.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
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

INSTALLED_APPS += (
    'django_cron',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'multimedia')
DOWNLOADS_ROOT = MEDIA_ROOT + 'downloads/'

FILMS_ROOT = MEDIA_ROOT + 'films/'
FILMS_URL = '/multimedia/films/'

SHOWS_ROOT = MEDIA_ROOT + 'shows/'
SHOWS_URL = '/multimedia/shows/'

LIST_LIMIT = 5
