from django.shortcuts import render, HttpResponse, redirect
from models import Course

# Create your views here.
def index(request):
    context = {
        'all_da_courses': Course.objects.all().order_by('-created_at')
    }
    return render(request, "manage_courses/index.html", context)

def add_course(request):
    server_name = request.POST['html_name']
    server_description = request.POST['html_description']
    Course.objects.create(name=server_name, description=server_description)
    return redirect('manage_courses:home')

def remove(request, class_id):
    Course.objects.filter(id=class_id).delete()
    return render(request, 'manage_courses/destroy.html')