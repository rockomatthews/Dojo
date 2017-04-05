from django.shortcuts import render, redirect
import re
from django.contrib import messages

def index(request):
    return render(request, 'user_app/index.html')

def register(request):
    if request.method == 'POST'
        
    

def login(request):
    if request.method == 'POST':
        server_first_name = request.POST['first_name']