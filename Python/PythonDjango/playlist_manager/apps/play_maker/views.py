from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = {
        'playlists':Playlist.objects.all()
    }
    return render(request, 'play_maker/index.html', context)

def add_playlist(request):
    playlist_name = request.POST['playlist_name']
    try:
        playlist.objects.create(name=playlist_name)
    except:
        messsages.error(request, 'Name is duplicate. Make a new name or add to the same existing list if that is your mood and you did not realize it')
    return redirect('pytunes:home')