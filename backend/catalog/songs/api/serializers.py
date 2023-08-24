from catalog.songs.models import Album, AlbumSong, Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = ('name', )


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name', )
        depth = 1


class AlbumSongSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(
        source='song.id',
    )
    name = serializers.ReadOnlyField(
        source='song.name',
    )


    class Meta:
        model = AlbumSong
        fields = ('id', 'position', 'name', )


class AlbumSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()
    songs = AlbumSongSerializer(
        source='albumsong_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Album
        fields = ('name', 'year', 'singer', 'songs', )
