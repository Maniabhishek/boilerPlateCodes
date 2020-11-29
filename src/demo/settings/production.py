from .base import *

DEBUG = False

ALLOWED_HOSTS = ['IP-ADDRESS','WWW.MY-WEBSITE.COM']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'YOUR_DB_NAME',
        'USER':'YOUR_DB_USER',
        'PASSWORD':'YOUR_DB_PASSWORD',
        'HOST': 'YOUR_DB_HOST',
        'PORT':'',
    }
}

