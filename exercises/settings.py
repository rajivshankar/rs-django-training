"""
Django settings for exercises project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# -*- coding: UTF-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from utils.misc import get_git_changeset

PROJECT_NAME = "exercises"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MEDIA_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, "media")
STATIC_ROOT = os.path.join(PROJECT_PATH, PROJECT_NAME, "static")

STATICFILES_DIRS = (
                    os.path.join(PROJECT_PATH, PROJECT_NAME, "site_static"),
                    )
# TEMPLATE_DIRS = (
#                  os.path.join(PROJECT_PATH, PROJECT_NAME, "templates"),
#                  )
LOCALE_PATHS = (
                os.path.join(PROJECT_PATH, "locale"),
                )
FILE_UPLOAD_TMP_DIR = os.path.join(PROJECT_PATH, PROJECT_NAME, "tmp")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9-m_!k-1io_4u5(-f$-@aaud4)xbpd#x*ejy(6=(kj_nynus#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapp1',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'exercises.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                     (
                     os.path.join(PROJECT_PATH, PROJECT_NAME, "templates"),
                     )
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

WSGI_APPLICATION = 'exercises.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/%s/' % get_git_changeset(PROJECT_PATH)

LANGUAGE_CODE = 'en'

LANGUAGES = (
             ("en", u"English"),
             ("de", u"Deutsche"),
             ("fr", u"Francaise"),             
)

######### The following section should be at the end of this file #########

try:
    execfile(os.path.join(APP_DIR, "local_settings.py"))
except IOError:
    pass
