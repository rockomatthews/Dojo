from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^add_artist$', views.add_artist, name="add_artist")
]