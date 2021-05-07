import os
from .base import *

SECRET_KEY = 'z+ksf@)0d^qojbh4rnp4b1to$hq&*tt(3bs$gf(3i267g$k9ln'
DEBUG = False
ALLOWED_HOSTS = ['192.168.0.101:8000','*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
