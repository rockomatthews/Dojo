from __future__ import unicode_literals

from django.db import models
from ..pipedreams.models import User
from ..wish_app.models import Item

class Wishlist(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Addition(models.Model):
    wishlist = models.ForeignKey(Wishlist, related_name='items')
    item = models.ForeignKey(Item, related_name='wishes')
    created_at = models.DateTimeField(auto_now_add=True)

class Otherlist(models.Model):
    others_item = models.ForeignKey(Item, related_name='items')
    other_user = models.ForeignKey(User, related_name="users")
    wishlist = models.ForeignKey(Wishlist, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)