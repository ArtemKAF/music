from django.apps import AppConfig  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore


class SongsApp(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog.songs'
    verbose_name = _('Songs')
