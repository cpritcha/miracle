# Production Django settings
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.comses.net']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'miracle_metadata',
        'USER': 'miracle',
        'PASSWORD': '',
    },
    'datasets': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'miracle_data',
        'USER': 'miracle',
        'PASSWORD': '',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# disabling i18n until we need it
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'CUSTOMIZE THIS'

SOCIAL_AUTH_FACEBOOK_KEY = 'customize this local secret key'
SOCIAL_AUTH_FACEBOOK_SECRET = 'customize this local secret key'

SOCIAL_AUTH_TWITTER_KEY = 'customize this local secret key'
SOCIAL_AUTH_TWITTER_SECRET = 'customize this local secret key'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''

if not os.path.exists(MEDIA_ROOT):
    print("MEDIA_ROOT path '{}' does not exist, trying to create it now.".format(MEDIA_ROOT))
    try:
        os.makedirs(MEDIA_ROOT)
    except:
        print("Unable to create path {}, user uploads will not work properly.".format(MEDIA_ROOT))

RAVEN_CONFIG = {
    'dsn': '',
}
