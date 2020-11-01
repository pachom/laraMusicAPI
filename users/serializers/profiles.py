"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# LaramusciAPI
from laramusicAPI.serializers import MusicListSerializer, MusicTrackSerializer
from laramusicAPI.models import MusicList

# Models
from users.models import Profile, MusicListInProfile




class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    musiclists = MusicListSerializer(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'biography',
            'visits',
            'listened_tracks',
            'reputation',
            'musiclists'
        )
        read_only_fields = (
            'visits',
            'listened_tracks',
            'reputation'
        )

    def create(self, validated_data):
        musiclists_data = validated_data.pop('musiclists')
        profile = Profile.objects.create(**validated_data)
            
        return profile


class MusicListInProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicListInProfile
        fields = ['id', 'musiclist', 'profile']

