from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hotdogs are by far the best food")