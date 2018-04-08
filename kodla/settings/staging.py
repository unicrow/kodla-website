# Local Django
from .base import *
from .secrets import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL, EMAIL_HOST_PASSWORD


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


ADMINS = (
    # ("Your Name", "your_email@example.com"),
)


# App used only at development
INSTALLED_APPS += (

)


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kodladb',
        'USER': 'kodla',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Domain

DOMAIN = 'https://www.kodla.co'


from .local import *
