from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'interview_db',
    }
}

ALLOWED_HOSTS = ['*']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'test'

INSTALLED_APPS += (
    'autofixture',
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
