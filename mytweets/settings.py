# -*- coding: utf-8 -*-

# Стройте пути к проекту как здесь: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Настройки разработчика для быстрого старта – для производства не годятся
# Посмотрите https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ: Сохраняйте секретный ключ, используемый в производстве, в секрете!
SECRET_KEY = 'l@y^@ra9q(ws(amb*-$wyc&_w@)1)s!p4r04rq9od$nr_*3!nx'

# ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ: Не запускайте в производство, если режим отладки включен!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Определение приложений
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_profile',
    'tweets',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mytweets.urls'

WSGI_APPLICATION = 'mytweets.wsgi.application'

# База данных
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    }
	}

STATICFILES_DIRS = (
BASE_DIR + '/static/',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'