from .base import *

from add_info import *

DEBUG = False

ADMINS = (
    ('Vanya K', os.environ.get('EMAIL_USER')),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {

    }
}
