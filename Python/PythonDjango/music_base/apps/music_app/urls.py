from django.conf.urls import url
from views import *

# Create your views here.
urlpatterns = [
   url(r'^$', index, name='music_route')
]