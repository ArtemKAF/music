from typing import OrderedDict, Union

from catalog.songs.models import Album, Singer  # isort: skip

class AlbumData(OrderedDict):
    name: str
    singer: Singer
    year: int
    songs: list[OrderedDict[str, Union[str, int]]]

def add_songs(
            self,
            instance: Album,
            songs: list[OrderedDict[str, Union[str, int]]]
        ) -> None: ...

def create(self, validated_data: AlbumData) -> Album: ...

def update(
            self,
            instance: Album,
            validated_data: AlbumData
        ) -> Album: ...

def to_representation(self, instance: Album) -> OrderedDict: ...

def validate(self, data: AlbumData) -> AlbumData: ...
