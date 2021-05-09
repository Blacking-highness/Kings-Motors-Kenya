import os
from .base import *

with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False
ALLOWED_HOSTS = ['192.168.0.101:8000','*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'static/images/media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images/media')