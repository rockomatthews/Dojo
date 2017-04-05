from __future__ import unicode_literals

from django.db import models
from ..wishlist_app.models import Wishlist

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=64)
    wishlist = models.ForeignKey(Wishlist, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)