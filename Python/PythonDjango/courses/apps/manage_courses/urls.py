from django.conf.urls import url
from views import *
from . import views

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^add_course/$', add_course, name='add_course'),
    url(r'^remove/(?P<class_id>\d+)$', remove, name='remove')
]