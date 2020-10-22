"""Lara mucsic models."""

# Django
from django.db import models
from django.dispatch import receiver


# Users
from users.models import Profile



class Artist(models.Model):
    name = models.CharField(max_length=10)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=100, blank=True)
    album_year= models.PositiveIntegerField(default=0)
    album_length = models.FloatField(
        default=0.0,
        help_text="Album time in minutes."
    )


class MusicTrack(models.Model):
    title = models.CharField(max_length=100, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.FloatField(
        default=0.0,
        help_text="track time in minutes."
    )
    views = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=2, blank=True)
    song_year = models.PositiveIntegerField(default=0)
    record_company = models.CharField(max_length=100, blank=True)
    likes = models.PositiveIntegerField(default=0)

class TypeList(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class MusicList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, blank=True)
    type_list = models.CharField(max_length=50, blank=True)
    tracks = models.ManyToManyField(MusicTrack, through='TrackInList')


class TrackInList(models.Model):
    musiclist = models.ForeignKey(MusicList, on_delete=models.CASCADE)
    musictrack = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)
    visits = models.PositiveIntegerField(default=0)

class History(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    musictrack = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)
    date_time = models.DateTimeField(
        'last played date at',
        auto_now_add=True,
        help_text='Date time on which the object was view.'
    )

