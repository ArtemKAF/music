from catalog.songs.models import Album, AlbumSong, Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class AlbumSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumSong
        fields = '__all__'
