##################################################################
FileName        = 'settings.py'
# By:            Jason Thorne
# Date:            15-06-2014
# Description:     The archeologist project
##################################################################
# Django settings for relics project.
import os
import datetime, time

DEBUG=False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
# THUMBNAIL_BACKEND = 'sorl.thumbnail.base.ThumbnailBackend'
# THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.cached_db_kvstore.KVStore'


########################################## 
def dateFromString(dateString, dateFormat, useTime):
    strippedTime    = time.strptime(dateString, dateFormat)
    myTime            = time.mktime(strippedTime)
    if useTime:
        retVal        = datetime.datetime.fromtimestamp(myTime)
        #retVal        = retVal.date()
    else:
        retVal        = datetime.date.fromtimestamp(myTime)
        retVal        = retVal.date()
    # end if
    
    return retVal
# end dateFromString
#######################################################################
def myDecrypt(myPasswd):
    retVal                = ''
    for i in myPasswd:
        retVal            += chr(ord(i) - 5)
    # next i
    
    return retVal

#######################################################################

### CUSTOM SETTINGS ###
# Akseli Palen 2013-01-30
#
# PROJECT_ROOT
#   Absolute path to the directory of this file (settings.py).
#   Will be helpful when absolute filesystem paths are required.
#   http://www.ramavadakattu.com/top-10-tips-to-a-new-django-developer
# r139
PROJECT_ROOT             = os.path.join(os.path.normpath(os.path.dirname(__file__)), '../')

ADMINS                     = (
    ('Jason Thorne', 'jthorne@magiclamp.com.au'),
)

MANAGERS                 = ADMINS

# moved to local.py
"""DATABASES                 = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'magiclamp$archives',                      # Or path to database file if using sqlite3.
        'USER': 'magiclamp',                      # Not used with sqlite3.
        'PASSWORD': 'magiclamp',                  # Not used with sqlite3.
        'HOST': 'magiclamp.mysql.pythonanywhere-services.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}"""


# where do we go to login?
LOGIN_URL               = '/archives/login'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE                 = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE            = 'en-us'

SITE_ID                 = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N                 = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N                 = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ                    = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT                 = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL                 = '/media/'

FILE_UPLOAD_PERMISSIONS = 0644

# Security wise this is a really good idea. It destroys the cookie when the browser closes, and
# I think it also takes the browser default in destroying the cookie after a certain
# amount of time
SESSION_EXPIRE_AT_BROWSER_CLOSE            = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT             = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL                 = '/static/'


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fn&amp;)67r^m9y#nce(0@&amp;(!9&amp;jjod2wvfbyg1@w5%17q_jzplj@a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'archeologist.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'archeologist.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    # thumbnails
    'sorl.thumbnail',
    
    'archives',
                  
    'survey',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#  use gmail for sending emails
EMAIL_HOST            = 'SMTP.GMAIL.COM'
EMAIL_PORT            = '587'
EMAIL_HOST_USER    = 'lokiWebmaster@gmail.com'
EMAIL_HOST_PASSWORD = 'sivaraman'
EMAIL_USE_TLS        = True

ALLOWED_HOSTS = [
    '.archive.science.mq.edu.au', # Allow domain and subdomains
    'localhost'
]

BING_KEY            = 'AoaUFrnhBNJZNwnVf2kj3uvLg0SQHr21pjs_8E7nI4NphT7QT3W-fDDUA7PJoyhk'

# import local settings
try:
    from local import *
except ImportError:
    pass
