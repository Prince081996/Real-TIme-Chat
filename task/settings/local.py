from task.settings.base import *
import os
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST':'127.0.0.1',
        'NAME': 'chat_db',
        'PORT':5432,
        'USER':'prince',
        'PASSWORD':'prince@1996'
    }
}
