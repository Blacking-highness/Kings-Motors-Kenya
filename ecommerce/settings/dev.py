from .base import *

SECRET_KEY = 'z+ksf@)0d^qojbh4rnp4b1to$hq&*tt(3bs$gf(3i267g$k9ln'
DEBUG = True
ALLOWED_HOSTS = ['*']

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images')
