"""
Django settings for xanana project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.locale
import logging
logger = logging.getLogger(__name__)
from django.utils.translation import ugettext_lazy as _
from django.conf import global_settings
try:
    from . import secrets
except ImportError:
    logger.error('Secrets could not be imported')
    secrets = {}

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "home",
    "search",
    "wagtail.wagtailforms",
    "wagtail.wagtailredirects",
    "wagtail.wagtailembeds",
    "wagtail.wagtailsites",
    "wagtail.wagtailusers",
    "wagtail.wagtailsnippets",
    "wagtail.wagtaildocs",
    "wagtail.wagtailimages",
    "wagtail.wagtailsearch",
    "wagtail.wagtailadmin",
    "wagtail.wagtailcore",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrapform",
    "rosetta",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.wagtailcore.middleware.SiteMiddleware",
    "wagtail.wagtailredirects.middleware.RedirectMiddleware",
]


ROOT_URLCONF = "xanana.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ]
        },
    }
]

WSGI_APPLICATION = "xanana.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getattr(secrets, 'DATABASE_NAME', os.environ.get('DATABASE_NAME', 'readingroom')),
        'USER': getattr(secrets, 'DATABASE_USER', os.environ.get('DATABASE_USER', 'readingroom')),
        'PASSWORD': getattr(secrets, 'DATABASE_PASWORD', os.environ.get('DATABASE_PASWORD', 'readingroom')),
        'HOST': getattr(secrets, 'DATABASE_HOST', os.environ.get('DATABASE_HOST', 'localhost')),
        'PORT': getattr(secrets, 'DATABASE_PORT', os.environ.get('DATABASE_PORT', '5432')),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/


TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "xanana"
LANGUAGE_CODE = "en"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "https://http://xananagusmaoreadingroom.com"

gettext = lambda s: s

LANGUAGES = (
    ("tet", gettext("Tetun")),
    # ('pt', _('Portuguese')),
    ("en", _("English")),
)

LOCALE_PATHS = [
    os.path.join(PROJECT_DIR, "../locale"),
    # os.path.join(PROJECT_DIR, 'xanana','locale'),
]


EXTRA_LANG_INFO = {
    "tet": {
        "bidi": True,  # right-to-left
        "code": "tet",
        "name": "Tetun",
        "name_local": "Tetun",  # unicode codepoints here
    }
}

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI + ["tet"]


ROSETTA_ENABLE_REFLANG = True
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_SHOW_AT_ADMIN_PANEL = True

try:
    from . import settings_local
except ImportError:
    pass
