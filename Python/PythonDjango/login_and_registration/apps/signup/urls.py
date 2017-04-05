from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_reg$', process_reg, name='process_reg'),
    url(r'^process_log$', process_log, name='process_log'),
]