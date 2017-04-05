from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^add$', add_playlist, name="add")
]

