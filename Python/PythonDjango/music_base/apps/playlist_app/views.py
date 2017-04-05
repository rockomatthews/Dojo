from django.shortcuts import render, redirect
import re
from django.contrib import messages

def index(request):
    return render(request, 'playlist_app/index.html')