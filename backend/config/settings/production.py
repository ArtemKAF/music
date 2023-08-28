from .base import *  # noqa

DEBUG = env.bool('DEBUG', False)

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default='')  # noqa
