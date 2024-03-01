"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jf$ax!sf0v2j0g(kv%omsdi*#+-hj9v&(h0g__)djm_-u1kny)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'captcha',
    'precise_bbcode',
    'bootstrap4',
    'django_cleanup',
    'easy_thumbnails',

    'bboard',
    'testapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'file_charset': 'utf-8',
            # 'debug': False, # uje est
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth', # user.is_authenticated, perms = param
                'django.contrib.messages.context_processors.messages',

                # 'django.template.context_processors.csrf',
                'django.template.context_processors.static',
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "12345",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# ABSOLUTE_URL_OVERRIDES = {
#     # 'bboard.rubric': lambda rec: "/%s" % rec.pk,
#     'bboard.rubric': lambda rec: f"/{rec.pk}/",
# }

# LOGIN_URL = "/accounts/login/"
LOGIN_URL = "bboard:login"
LOGIN_REDIRECT_URL = "bboard:index"
LOGOUT_REDIRECT_URL = "bboard:index"

# CAPTCHA
CAPTCHA_CHALLENGE_FUNC = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 4  # 6
CAPTCHA_WORDS_DICTIONARY = '/static/captcha_words.txt'
CAPTCHA_TIMEOUT = 5  # MINUTES


# DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440   # 2.5 MBYTES
# DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

## BBCode
BBCODE_NEWLINE = "<br>"
# BBCODE_ESCAPE_HTML
BBCODE_DISABLE_BUILTIN_TAGS = False
BBCODE_ALLOW_CUSTOM_TAGS = True
BBCODE_ALLOW_SMILIES = True
BBCODE_SMILIES_UPLOAD_TO = os.path.join('precise_bbcode', 'smilies')

# BOOTSTRAP4 = {
#     'horizontal_label_class': 'col-md-3',
#     'horizontal_field_class': 'col-md-9',
#     'required_css_class': '',
#     'success_css_class': 'has-success',
#     'error_css_class': 'has-error',
# }

THUMBNAIL_ALIASES = {
    'bboard.Bb.picture' : {
        'default': {
            'size' : (500,300),
            'crop' : 'scale',
        },
    },
    'testapp' : {
        'default': {
            'size' : (400,300),
            'crop' : 'smart',
            'bw' : True,
        },
    },
    '':{
        'default' : {
            'size' : (180,240),
            'crop' : "scale"
        },
        'big':{
            'size':(480, 640),
            'crop':'10,10'
        },
    },
}

THUMBNAIL_DEFAULT_OPTIONS = {
    'quality' : 90,
    'subsampling' : 1
}

THUMBNAIL_PRESERVE_EXTENSION = True #('png',)
