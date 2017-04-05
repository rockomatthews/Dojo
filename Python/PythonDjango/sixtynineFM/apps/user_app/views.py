import re
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    if 'user_id' in request.session:
        return redirect('playlist:home')
    
    return render(request, 'user_app/index.html')

def login(request):
    
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']
    try:
        user = User.objects.get(email=server_email)
        if user.password == server_password:
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['user_name'] = user.first_name + " " + user.last_name
            return redirect('playlist:home')
        else:
            messages.error(request, 'you botched your password')
            return redirect('user:home')
    except:
        messages.error(request, 'email deos not exist or was entered wrong (which still means it does not exist)')
        return redirect('user:home')

def register(request):
    if request.method == 'POST':
        server_first_name = request.POST['html_first_name']
        server_last_name = request.POST['html_last_name']
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        server_password_confirm = request.POST['html_password_confirm']

        is_valid = True


        if len(server_first_name) < 2 or len(server_last_name) < 2:
            messages.error(request, 'first name or last name needs to grow a bit buddy')
            is_valid = False

        if EMAIL_REGEX.search(server_email) is None:
            messages.error(request, 'email address must be an email address.  IF you want it to look different, talk to the president of the internet')
            is_valid = False

        if (server_password_confirm != server_password) or len(server_password_confirm) < 5:
            messages.error(request, "passwords don't match.  Do we have to make it visible for you baaaaby.  are you a child?? type right")
            is_valid = False
        
        if is_valid:
            try:
                user = User.objects.create(first_name=server_first_name, last_name=server_last_name, email=server_email, password=server_password)
                request.session['user_id'] = user.id
                request.session['user_name'] = user.first_name + " " + user.last_name
                return redirect('playlist:home')
            except:
                messages.error(request, "this email already exists!")
                return redirect('user:home')
        else:
            return redirect('user:home')
    else:
        return redirect('user:home')

def profile(request):
    
    return render(request, 'user_app/profile.html')

def edit_profile(request):
    return render(request, 'user_app/edit_profile.html')

def save(request):
    if request.method == 'POST':
        new_first_name = request.POST['html_first_name']
        new_last_name = request.POST['html_last_name']
    
        user = User.objects.get(id=request.session['user_id'])
        
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.save()

        request.session['new_first_name'] = user.first_name
        request.session['new_last_name'] = user.last_name
        request.session['user_name'] = user.first_name + " " + user.last_name
        return redirect('user:profile')
    

def logout(request):
    request.session.clear()
    return redirect('user:home')