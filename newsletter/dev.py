from settings import *

# Django Secret Key
SECRET_KEY = 'hc=mut37gj_kq3*9v2_371-_ib)=iyc%!0hs!nfl8ak%lf6@)x'

# Debug mode
DEBUG = True

TEMPLATE_DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newsletter',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '/tmp/mysql.sock',
        'PORT': '',
    }
}
