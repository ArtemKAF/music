from .base import *  # noqa

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default='')  # noqa
