from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
# Create your views here.
    return render(request, 'signup/index.html')

def process_reg(request):
    if request.method == 'POST':
    server_first_name = request.POST['html_first_name']
    return render(request, 'signup/sucess.html')

def process_log(request):
    return render(request, 'signup/sucess.html')