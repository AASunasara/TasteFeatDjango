from srvdy.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['sarvodaysweets.herokuapp.com',]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'srvdy',
        'USER': 'root',
        'PASSWORD': '8118aass',
        'HOST': 'sarvodaysweets.herokuapp.com',
        'PORT':'',

        }
}
