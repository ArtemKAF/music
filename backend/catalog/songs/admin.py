from django.contrib import admin  # type: ignore

from catalog.songs.models import Album, AlbumSong, Singer, Song  # isort: skip


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    ...


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    ...


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    ...


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    ...
