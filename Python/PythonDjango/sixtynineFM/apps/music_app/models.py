from __future__ import unicode_literals

from django.db import models
from ..user_app.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(unique=True, max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(Artist, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    album = models.ForeignKey(Album, related_name="songs")
    title = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fan(models.Model):
    artist = models.ForeignKey(Artist, related_name='users')
    user = models.ForeignKey(User, related_name='artists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)