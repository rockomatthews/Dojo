from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^process$', views.process, name='process'),
    url(r'^success$', views.success, name='success'),
    url(r'^go_back$', views.go_back, name='go_back')
]