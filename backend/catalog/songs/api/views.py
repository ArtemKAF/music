from rest_framework import viewsets

from ..api.serializers import (AlbumSerializer, AlbumSongSerializer,
                               SingerSerializer, SongSerializer)
from ..models import Album, AlbumSong, Singer, Song


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
