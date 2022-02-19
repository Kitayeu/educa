from .base import *

from add_info import *

DEBUG = False

ADMINS = (
    ('Vanya K', os.environ.get('EMAIL_USER')),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}
