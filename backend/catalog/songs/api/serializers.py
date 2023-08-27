from catalog.songs.models import Album, AlbumSong, Singer, Song
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = ('name', )


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('name', )


class AlbumSongReadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source='song.name',
        read_only=True,
    )

    class Meta:
        model = AlbumSong
        fields = ('name', 'position', )


class AlbumSongWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = AlbumSong
        fields = ('name', 'position', )


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Singer.objects.all()
    )
    songs = AlbumSongWriteSerializer(
        many=True,
        required=True,
    )

    class Meta:
        model = Album
        fields = ('name', 'year', 'singer', 'songs', )

    def add_songs(self, instance, songs):
        for song in songs:
            position = song.pop('position')
            song = Song.objects.get_or_create(**song)[0]
            instance.songs.add(
                song, through_defaults={
                    'position': position
                }
            )

    def create(self, validated_data):
        songs = validated_data.pop('songs')
        album = super().create(validated_data)
        self.add_songs(album, songs)
        return album

    def update(self, instance, validated_data):
        if 'songs' in validated_data:
            songs = validated_data.pop('songs')
            AlbumSong.objects.filter(album=instance).delete()
            self.add_songs(instance, songs)
        super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):
        self.fields['songs'] = AlbumSongReadSerializer(
            source='albumsongs',
            many=True
        )
        return super().to_representation(instance)

    def validate(self, data):
        errors = {}
        if self.context.get('request').method == 'POST':
            if Album.objects.filter(
                name=data.get('name'),
                singer=data.get('singer')
            ).exists():
                errors['exists'] = _(
                    'This singer alredy has an album with this name!'
                )
        if len(data.get('songs')) != 0:
            songs = list(map(lambda x: x.get('name'), data.get('songs')))
            if len(songs) != len(set(songs)):
                errors['song_duptication'] = _(
                    'There can not be songs with the same name in an album!'
                )
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)
