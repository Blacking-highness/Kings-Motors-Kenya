from .base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = 'z+ksf@)0d^qojbh4rnp4b1to$hq&*tt(3bs$gf(3i267g$k9ln'

DEBUG = True
ALLOWED_HOSTS = ['*']

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

