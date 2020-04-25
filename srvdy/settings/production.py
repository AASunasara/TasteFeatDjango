from srvdy.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['sarvodaysweets.herokuapp.com',]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3bhet188vesg7',
        'USER': 'nxjdfpqemknhpt',
        'PASSWORD': '7718256152243b79a6f4355a3110b5c2905329ef9a7b9cde331c2450e98cf157',
        'HOST': 'ec2-34-193-232-231.compute-1.amazonaws.com',
        'PORT':'5432',

        }
}

import dj_database_url
DATABASES['default'] = dj_database_url.parse('postgres://nxjdfpqemknhpt:7718256152243b79a6f4355a3110b5c2905329ef9a7b9cde331c2450e98cf157@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d3bhet188vesg7', conn_max_age=600)