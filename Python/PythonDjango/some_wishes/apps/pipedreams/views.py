import re
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    return render(request, 'pipedreams/index.html')


def register(request):
    if request.method == 'POST':
        server_name = request.POST['html_name']
        server_username = request.POST['html_username']
        server_password = request.POST['html_password']
        server_confirm_password = request.POST['html_confirm_password']

        is_valid = True


        if len(server_name) < 3 or len(server_username) < 3:
            messages.error(request, 'your name and username both need to be at least 3 characters')
            is_valid = False

        if (server_password_confirm != server_password) or len(server_password_confirm) < 5:
            messages.error(request, "passwords don't match. please make them do so")
            is_valid = False
        
        if is_valid:
            try:
                user = User.objects.create(name=server_name, username=server_username, password=server_password)
                request.session['user_id'] = user.id
                return redirect('wishlist:home')
            except:
                messages.error(request, "this user already exists!")
                return redirect('pipedreams:home')
        else:
            return redirect('pipedreams:home')
    else:
        return redirect('pipedreams:home')
