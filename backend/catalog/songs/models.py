from django.db import models  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore

from catalog.songs.constants import (MAX_LENGHT_NAME,  # isort: skip
                                     MAX_SONG_IN_ALBUM_POSITION, MAX_YEAR,
                                     MIN_SONG_IN_ALBUM_POSITION, MIN_YEAR
                                     )
from catalog.songs.fields import (  # isort: skip
    ValidatePositiveSmallIntegerField
)
from catalog.songs.utils import get_help_text_required_max_chars  # isort: skip


class BaseModel(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=MAX_LENGHT_NAME,
        unique=True,
        blank=False,
        db_index=True,
        help_text=get_help_text_required_max_chars(
            MAX_LENGHT_NAME
        ),
    )

    class Meta:
        abstract = True
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Singer(BaseModel):

    class Meta:
        verbose_name = _('Singer')
        verbose_name_plural = _('Singers')


class Song(BaseModel):

    class Meta:
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')


class Album(BaseModel):
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        verbose_name=_('Singer'),
        blank=False,
    )
    year = ValidatePositiveSmallIntegerField(
        verbose_name=_('Year'),
        blank=True,
        min_value=MIN_YEAR,
        max_value=MAX_YEAR,
    )
    songs = models.ManyToManyField(
        Song,
        through='AlbumSong',
        through_fields=('album', 'song', ),
    )

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')
        default_related_name = 'albums'


class AlbumSong(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name=_('Album'),
        blank=False,
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name=_('Song'),
        blank=False,
    )
    position = ValidatePositiveSmallIntegerField(
        verbose_name=_('Position'),
        blank=False,
        min_value=MIN_SONG_IN_ALBUM_POSITION,
        max_value=MAX_SONG_IN_ALBUM_POSITION,
    )

    class Meta:
        ordering = ('position', )
        verbose_name = _('Song in album')
        verbose_name_plural = _('Songs in albums')
        default_related_name = 'albumsongs'
        constraints = (
            models.UniqueConstraint(
                fields=('album', 'song', ),
                name='%(app_label)s_%(class)s_unique_album_song',
            ),
        )

    def __str__(self) -> str:
        return f'{self.song} ' + _('in') + f' {self.album}'
