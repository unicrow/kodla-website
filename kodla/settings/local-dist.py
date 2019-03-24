# Local Django
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kodla',
        'USER': 'kodla',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': '',
    }
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Domain

DOMAIN = 'http://127.0.0.1:8000'
