from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    INSTALLED_APPS += (
        'debug_toolbar',
        'rest_framework_swagger',
    )

    INTERNAL_IPS = ['127.0.0.1', ]  # required for django debug toolbar
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
        'rest_framework.authentication.SessionAuthentication'  # do not use this on production
    )

BACKEND_URL = ""

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 5432,
    }
}

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '2525'

STATIC_ROOT = os.path.join(ROOT_DIR, 'static/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media/')
MEDIA_URL = '/media/'

ALLOWED_FILE_FORMATS = ['pdf', 'docx', 'doc', 'xlsx', 'xls', 'csv', 'txt']
ALLOWED_IMAGE_FORMATS = ['jpg', 'png', 'jpeg']
ALLOWED_VIDEO_FORMATS = ['mp4', ]
