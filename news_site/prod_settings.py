from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-gbbhs345-3nvdmq-)l39*fw8342t%nc(@x(-i4y6)nd^)pb-d2#^6g9+@gy'

DEBUG = False

ALLOWED_HOSTS = ['NewsSiteMlazar.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news',
        'USER': 'magister',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'news/static'
    ]


STATIC_ROOT = BASE_DIR / 'assets'
