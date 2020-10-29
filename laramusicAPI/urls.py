"""LaramusicAPI Urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from laramusicAPI import views as laramusic_views


router = DefaultRouter()
router.register(r'artists', laramusic_views.ArtistViewSet, basename='artists')
router.register(r'albums', laramusic_views.AlbumViewSet, basename='albums')
router.register(r'musiclists', laramusic_views.MusicListViewSet, basename='musiclists')
router.register(r'musictracks', laramusic_views.MusicTrackViewSet, basename='musictracks')
router.register(r'typelists', laramusic_views.TypeListViewSet, basename='typelists')
router.register(r'trackinlists', laramusic_views.TrackInListViewSet, basename='trackinlists')
router.register(r'histories', laramusic_views.HistoryViewSet, basename='histories')

urlpatterns = [
    path('', include(router.urls))
]