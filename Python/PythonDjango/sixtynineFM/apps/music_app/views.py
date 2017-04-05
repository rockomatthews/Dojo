import re
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import Artist

def index(request):
    if 'user_id' in request.session:
        return redirect('playlist:home')

    return render(request, 'user_app/index.html')

def add_artist(request, artist_name):
    if request.method == "POST":
        server_add_artist_name = request.POST['html_add_artist_name']
        try:
            context = {
                'name': artist_name,
            }
            artist = Artist.objects.create(name=server_add_artist_name)
            request.session['artist_name'] = artist.name
            return redirect('playlist:home', artist_name)
        except:
            messages.error(request, 'artist already exists. try adding another')
            return redirect('playlist:home')
    return redirect('music:home')