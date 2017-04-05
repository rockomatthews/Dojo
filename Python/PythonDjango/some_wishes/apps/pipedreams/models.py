from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    date_hired = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
