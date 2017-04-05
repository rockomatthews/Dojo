from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)