from django.conf.urls import url
from views import *
from . import views

urlpatterns = [
    url(r'^$', index),
    url(r'^process$', views.results),
    url(r'^return$', views.go_back)
]