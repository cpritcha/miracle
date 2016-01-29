# Production Django settings
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.comses.net']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RAVEN_CONFIG = {
    'dsn': '',
}
