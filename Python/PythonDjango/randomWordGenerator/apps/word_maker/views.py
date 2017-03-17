from django.shortcuts import render, redirect, HttpResponse
import string
import random



# Create your views here.
def index(request):
    return render(request, "word_maker/index.html")

def random_generator(request):
    the_count = 0
    if request.POST.get('generate') == 'generate':
        request.session['the_count'] += 1
    x = ''.join(random.choice(string.lowercase) for i in range(14))
    request.session['random_one'] = x
    return redirect('/')

