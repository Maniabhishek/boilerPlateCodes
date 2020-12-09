from .base import *

DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = ['IP-ADDRESS','WWW.MY-WEBSITE.COM']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB_NAME'),
        'USER':config('USER_NAME'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT':'',
    }
}

