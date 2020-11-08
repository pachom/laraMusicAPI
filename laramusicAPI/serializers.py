"""Lara music serializers."""

# Django Rest Framework
from rest_framework import serializers

# Models
from laramusicAPI.models import (Artist, Album,
    MusicTrack, TypeList,
    MusicList, TrackInList,
    History
)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'name',
            'fuente',
            'fuente_id',
            'fuente_uri',
            'fuente_img',
        ]


class MusicTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicTrack
        fields = [
            'id',
            'order',
            'title',
            'fuente',
            'track_uri',
            'image_uri',
            'artist',
            'album_uri',
            'length',
            'views',
            'gender',
            'song_year',
            'record_company',
            'likes',
            'created',
            'modified',
        ]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Album
        fields = ['id', 'album_title', 'artist', 'album_year', 'album_length', 'tracks']


class TypeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeList
        fields = ['name',]


class MusicListSerializer(serializers.ModelSerializer):
    musictracks = MusicTrackSerializer(many=True)

    class Meta:
        """Meta class."""

        model = MusicList
        fields = ['id', 'title', 'type_list', 'created', 'modified', 'musictracks']
        read_only_fields = ['created', 'modified']


    def create(self, validated_data):
        tracks_data = validated_data.pop('musictracks')
        musiclist = MusicList.objects.create(**validated_data)
        for track_data in tracks_data:
            track = MusicTrack.objects.create(musiclist=musiclist, **track_data)
            m1 = TrackInList(musiclist=musiclist, musictrack=track)
            m1.save()
        return musiclist


class TrackInListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackInList
        fields = ['id', 'musiclist', 'musictrack', 'visits',]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id',  'musictrack', 'date_time',]
        