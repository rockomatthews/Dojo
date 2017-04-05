import re
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    return render(request, 'wish_app/index.html')