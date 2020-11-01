"""Profile model."""

# Django
from django.db import models

# LaramusicAPI
from laramusicAPI.models import MusicList

# Utilities
from utils.models import Lara_apiModel


class Profile(Lara_apiModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    visits = models.PositiveIntegerField(default=0)
    listened_tracks = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the continuos visits."
    )

    musiclists = models.ManyToManyField(MusicList, through='MusicListInProfile')

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)

class MusicListInProfile(Lara_apiModel, models.Model):
    musiclist = models.ForeignKey(MusicList, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

