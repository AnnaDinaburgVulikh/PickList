from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'eventlist/home.html', context)


def about(request):
    return render(request, 'eventlist/about.html', {'title': 'About'})