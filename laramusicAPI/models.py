"""Lara mucsic models."""

# Django
from django.db import models
from django.dispatch import receiver


# Users
from users.models import Profile

# Utils
from utils.models import Lara_apiModel



class Artist(Lara_apiModel, models.Model):
    name = models.CharField(max_length=100)
    fuente = models.CharField(max_length=100, blank=True) 
    fuente_id = models.CharField(max_length=100, blank=True) 
    fuente_uri = models.URLField(blank=True)
    fuente_img = models.URLField(blank=True)

class Album(Lara_apiModel, models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=100, blank=True)
    album_year= models.PositiveIntegerField(default=0)
    album_length = models.FloatField(
        default=0.0,
        help_text="Album time in minutes."
    )


class MusicTrack(Lara_apiModel, models.Model):
    title = models.CharField(max_length=100)
    uri = models.URLField(blank=True)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    length = models.FloatField(
        default=0.0,
        help_text="track time in minutes."
    )
    views = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=2, blank=True)
    song_year = models.PositiveIntegerField(default=0)
    record_company = models.CharField(max_length=100, blank=True)
    likes = models.PositiveIntegerField(default=0)
    order = models.IntegerField(default=1)
    tempo = models.IntegerField(default=0)
    time_sig = models.IntegerField(default=0)
    key_of = models.CharField(max_length=20, blank=True)
    camelot = models.CharField(max_length=20, blank=True) 

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)


class MusicList(Lara_apiModel, models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, blank=True)
    type_list = models.CharField(max_length=50, blank=True)
    musictracks = models.ManyToManyField(MusicTrack, through='TrackInList')
    

class TrackInList(Lara_apiModel, models.Model):
    musiclist = models.ForeignKey(MusicList, on_delete=models.CASCADE)
    musictrack = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)
    visits = models.PositiveIntegerField(default=0)


class TypeList(Lara_apiModel, models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    class Meta:
        ordering = ['name']

class History(Lara_apiModel, models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    musictrack = models.ForeignKey(MusicTrack, on_delete=models.CASCADE, null=True)
    listened_uri = models.URLField(blank=True)
    date_time = models.DateTimeField(
        'last played date at',
        auto_now_add=True,
        help_text='Date time on which the object was view.'
    )

