from pathlib import Path
import os
from dj_database_url import config as config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', default='sdfjvsadifhu!@$!248236754235sdyvfgb2!@1896QAW3G97FR16!@#$@$¨#%&3gSDfDGp')

DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['localhost']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'administradores',
    'users'
]


AUTH_USER_MODEL = 'users.Usuarios'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myrole.routes'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "WEB",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myrole.wsgi.application'

default_dburl = 'mysql://root:1234@localhost:3306/db_myrole'

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default= default_dburl,
        conn_max_age=600
    )
}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Etc/GMT-4'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/accounts/auth/login'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics-files'),
]

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticsfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediasfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
