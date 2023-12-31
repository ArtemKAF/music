from rest_framework import viewsets

from catalog.songs.api.serializers import (
    AlbumSerializer, SingerSerializer, SongSerializer,
)
from catalog.songs.models import Album, Singer, Song


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
