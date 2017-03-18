from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request): 
    return render(request, 'survey_form/index.html')

def results(request):
    the_count = 0
    request.session['the_count'] += 1
    context = {
        'server_name': request.POST['your_name'],
        'server_lang': request.POST['favourite_language'],
        'server_location': request.POST['location'],  
        'server_comment': request.POST['comment'],   
    }
    return render(request, 'survey_form/results.html', context)

def go_back(request):
    return render(request, 'survey_form/index.html')
