"""
Django settings for aishack project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = "thisisasecretkeyforyou"
DEBUG = True

if not DEBUG:
    assert(SECRET_KEY != "thisisasecretkeyforyou")

ALLOWED_HOSTS = ['.aishack.in', '127.0.0.1', 'localhost']

TEMPLATE_DEBUG = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aishack',
    #'south',
    'haystack',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aishack.urls'

WSGI_APPLICATION = 'aishack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = "/static/"
if os.name == 'nt':
    STATIC_ROOT = 'c:/work/aishack/aishack/static/'
else:
    STATIC_ROOT = '/work/aishack/aishack/static/'

STATICFILES_DIRS =(os.path.join(BASE_DIR, "static"),)
STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
                        "compressor.finders.CompressorFinder",)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

#############################################
# site specific settings
SITE_TITLE = "AI Shack"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9201',
        'INDEX_NAME': 'aishack_haystack',
    }
}
