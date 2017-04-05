from django.shortcuts import render, redirect
import re
from django.contrib import messages
from .models import Emails


# Create your views here.
def index(request):
    return render(request, "email_checker/index.html")

def process(request):
    # user_id = request.session
    if request.method == 'POST':
        server_email = request.POST['html_email']
        if len(server_email) < 1:
            messages.error(request, "NO EMAIL GIVEN")
            return redirect('email_checker:home')        
        if re.match('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', server_email):
            Emails.objects.create(email = server_email)
            return redirect('email_checker:success')
        else: 
            messages.error(request, "NOT AN EMAIL ADDRESS")
            return redirect('email_checker:home')

def success(request):
    last_email = Emails.objects.all().last
    context = {
        'last_email': last_email,
        'all_emails': Emails.objects.all()
    }
    return render(request, 'email_checker/success.html', context)

def go_back(request):
    return redirect('email_checker:home')