from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now().strftime('%-I:%M:%S')
    different_now = datetime.datetime.now().strftime('%B %d, %Y')
    context = {
        'da_time': now,
        'da_day': different_now
    }
    return render(request, "timedisplay/index.html", context)


