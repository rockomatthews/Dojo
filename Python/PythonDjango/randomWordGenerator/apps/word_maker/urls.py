from django.conf.urls import url
from views import *
from . import views

urlpatterns = [
    url(r'^$', index),
    url(r'^create_word$', views.random_generator)
]