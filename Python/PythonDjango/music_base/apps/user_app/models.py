from __future__ import unicode_literals

from django.db import models
from ..music_app.models import Artist, Album, Song, Fan
from ..playlist_app.models import Playlist, Addition, Listener

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    follower = models.ForeignKey(User, related_name='followees')
    followee = models.ForeignKey(User, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)