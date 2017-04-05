from __future__ import unicode_literals

from django.db import models
from ..playlist_app.models import Playlist, Addition, Listener
from ..user_app.models import User, Friend

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharFied(max_length=64)
    artist = models.ForeignKey(Artist, related_name='albums')
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    albums = models.ForeignKey(Albums, related_name='songs')
    title = models.CharFied(max_length=64)
    genre = models.CharFied(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fan(models.Model):
    user = models.ForeignKey(User, related_name='favorites_artists')
    playlist = models.ForeignKey(Playlist, related_name='fans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)