import os
from .base import *

with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = True
ALLOWED_HOSTS = ['192.168.0.101:8000','*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT  = 587
EMAIL_HOST_USER = 'pbubezi@gmail.com'
EMAIL_HOST_PASSWORD = '8dC60rHTN3VEYUwf'
EMAIL_USE_TLS = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'