from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Event
import datetime


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
    paginate_by = 4

    def get_queryset(self):
        return Event.objects.filter(date__gt=datetime.date.today())


class UserEventListView(ListView):
    model = Event
    template_name = 'eventlist/user_events.html'
    context_object_name = 'events'
    ordering = ['date']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(owner=user,
                                    date__gt=datetime.date.today()
                                    ).order_by('date')


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'location']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False


def about(request):
    return render(request, 'eventlist/about.html', {'title': 'About'})
