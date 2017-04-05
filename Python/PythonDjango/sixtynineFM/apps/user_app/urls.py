from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit_profile$', views.edit_profile, name='edit_profile'),
    url(r'^save$', views.save, name='save'),
    url(r'^logout$', views.logout, name='logout')
]