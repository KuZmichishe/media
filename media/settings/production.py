from media.settings.base import *

DEBUG = False

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