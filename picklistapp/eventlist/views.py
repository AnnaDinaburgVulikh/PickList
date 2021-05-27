from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)
from .models import Event
import datetime

# Create your views here.
def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'eventlist/home.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'eventlist/home.html'
    context_object_name = 'events'
    ordering = ['date']

    def get_queryset(self):
        return Event.objects.filter(date__gt=datetime.date.today())


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']


class EventDetailView(DetailView):
    model = Event

def about(request):
    return render(request, 'eventlist/about.html', {'title': 'About'})