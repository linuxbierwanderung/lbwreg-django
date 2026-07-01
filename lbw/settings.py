"""
Django settings for lbw project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', 'a_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ADMINS = (
    (os.getenv('ADMIN_NAME', 'Administrator'),
     os.getenv('ADMIN_EMAIL', 'nobody@nowhere.com')),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(' ')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Running Health Checks
    'health_check',
    'health_check.db',

    # dependencies
    'crispy_forms',
    'crispy_bootstrap4',

    # actual LBW apps
    'accounts',
    'registration',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lbw.urls'

WSGI_APPLICATION = 'lbw.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'lbw'),
        'CONN_MAX_AGE': int(os.getenv('DB_CONN_MAX_AGE', "0")),
        'USER': os.getenv('MYSQL_USER', 'lbw'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'password'),
        'HOST': os.getenv('MARIADB_HOST', None),
        'PORT': os.getenv('MARIADB_PORT', None),
        'OPTIONS': {'charset': 'utf8mb4', 'sql_mode': 'TRADITIONAL',
                    'init_command': 'SET '
                                    'default_storage_engine=INNODB,'
                                    'character_set_connection=utf8mb4,'
                                    'collation_connection=utf8mb4_bin;'
                                    'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
                    },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/var/www/content/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'https://content.draiocht.net/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# old settings ===================

SITE_ID = 1


# Media (user uploads)
#

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/var/www/content/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
if DEBUG:
    MEDIA_URL = '/media/'
else:
    MEDIA_URL = 'https://content.draiocht.net/media/'

# Templates

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
            'loaders': [
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',)), ],
            'string_if_invalid': ('Undefined variable used, please file a bug at '
                                  '<a href="http://github.com/lbedford/lbwreg.django">'
                                  'github</a>'),
        },
    },
]


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
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        # Custom handler which we will use with logger 'django'.
        # We want errors/warnings to be logged when DEBUG=False
        'console_on_not_debug': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins', 'console_on_not_debug'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# EMail settings
if os.getenv('EMAIL_CONSOLE_BACKEND', 'False').lower() == 'true':
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'from@lbw.com')
SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'server@lbw.com')

LBW_TO_EMAIL = [os.getenv('LBW_TO_EMAIL', 'to@lbw.com')]
LBW_FROM_EMAIL = os.getenv('LBW_FROM_EMAIL', 'from@lbw.com')

EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '25'))

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

if EMAIL_PORT == 465:
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = True
elif EMAIL_PORT == 587:
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False


DATE_FORMAT = 'Y-m-d'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# deployment settings for https
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

# settings.py


class InvalidVarException(object):
    """Invalid vars debugging."""
    def __mod__(self, missing):
        try:
            missing_str = str(missing)
        except Exception:
            missing_str = 'Failed to create string representation'
        raise Exception('Unknown template variable %r %s' %
                        (missing, missing_str))

    def __contains__(self, search):
        if search == '%s':
            return True
        return False


TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = InvalidVarException()
