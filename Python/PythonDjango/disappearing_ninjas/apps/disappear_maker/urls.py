from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.show_all_ninjas),
    url(r'^ninjas/(?P<color>\D+)$', views.show_ninja)
]








