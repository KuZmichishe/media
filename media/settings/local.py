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