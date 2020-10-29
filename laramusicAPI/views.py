"""Lara music views."""

# Rest_framework
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# LaramusicAPI
from laramusicAPI.models import (Artist, Album,
    MusicTrack, TypeList,
    MusicList, TrackInList,
    History
)
from laramusicAPI.serializers import (ArtistSerializer, 
    AlbumSerializer,
    MusicTrackSerializer,
    TypeListSerializer,
    MusicListSerializer,
    TrackInListSerializer,
    HistorySerializer
)


class ArtistViewSet(viewsets.ModelViewSet):
    """API endpoint that allows artists to be viewed or edited."""
    
    try:
        permission_classes = (IsAuthenticated,)
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer
        lookup_field = 'name'
    except:
        import sys
        print(sys.exc_info())
    


class AlbumViewSet(viewsets.ModelViewSet):
    """API endpoint that allows albums to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class MusicTrackViewSet(viewsets.ModelViewSet):
    """API endpoint that allows musictracks to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = MusicTrack.objects.all()
    serializer_class = MusicTrackSerializer


class TypeListViewSet(viewsets.ModelViewSet):
    """API endpoint that allows typelists to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = TypeList.objects.all()
    serializer_class = TypeListSerializer


class MusicListViewSet(viewsets.ModelViewSet):
    """API endpoint that allows musiclists to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = MusicList.objects.all()
    serializer_class = MusicListSerializer


class TrackInListViewSet(viewsets.ModelViewSet):
    """API endpoint that allows tracksinlist to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = TrackInList.objects.all()
    serializer_class = TrackInListSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows histories to be viewed or edited."""
    
    permission_classes = (AllowAny,)
    queryset = History.objects.all()
    serializer_class = HistorySerializer