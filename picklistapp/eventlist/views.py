from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Event, Items_to_bring, Invitees
import datetime


# basic pages
def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'eventlist/home.html', context)


def about(request):
    return render(request, 'eventlist/about.html', {'title': 'About'})


# Event views
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
    template_name = 'eventlist/itemslist_for_event.html'

    def get_object(self):
        return get_object_or_404(Event, pk=self.request.event.id)


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


# Event list views
def ItemslistForEvent(request, pk):
    event_id = pk
    item_event = Event.objects.filter(pk=event_id)[0]
    items_to_bring = Items_to_bring.objects.filter(event=item_event)
    # items_to_bring = Items_to_bring.objects.all()
    if request.method == "POST":
        if "itemAdd" in request.POST:
            name = request.POST["description"]
            amount = int(request.POST["amount"])
            itemsList = Items_to_bring(event=item_event,
                                       name=name,
                                       amount=amount)
            itemsList.save()
            return redirect(request.path_info)

        if "itemDelete" in request.POST:
            checkedlist = request.POST["checkedboxlist"].split(",")
            for item_id in checkedlist:
                itemsList = Items_to_bring.objects.get(id=int(item_id))
                itemsList.delete()
    return render(request,
                  "eventlist/itemslist_for_event.html",
                  {"event": item_event, "items": items_to_bring})
