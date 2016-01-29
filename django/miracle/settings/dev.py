# Local development Django settings overrides
from .base import *

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# disabling i18n until we need it
USE_I18N = False
