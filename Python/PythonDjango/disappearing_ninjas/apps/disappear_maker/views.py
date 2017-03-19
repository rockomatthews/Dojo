from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'disappear_maker/index.html')

def show_all_ninjas(request):
    return render(request, 'disappear_maker/all_ninjas.html')

def show_ninja(request, color):
    if color == 'red':
        color = 'red'
    elif color == 'blue':
        color = 'blue'
    elif color == 'orange':
        color = 'orange'
    elif color == 'purple':
        color = 'purple'
    else:
        color = 'yellow'
    context = {
        'color': color
    }
    return render(request, 'disappear_maker/show_the_ninja.html', context)