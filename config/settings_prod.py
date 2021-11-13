import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3(mytum)rh8$tjfidkvkwmw&g)6f_3^5wi#4g_4vku_rxeeqlo'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/std/kursach/db.sqlite3',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (STATIC_DIR,)