from django.urls import path
from .views import (EventListView,
                    EventCreateView,
                    EventUpdateView,
                    EventDeleteView,
                    UserEventListView,)
from . import views

urlpatterns = [
     path('',
          EventListView.as_view(),
          name='event-home'),
     path('user/<str:username>',
          UserEventListView.as_view(),
          name='user-events'),
     path('event/new/',
          EventCreateView.as_view(),
          name='event-create'),
     path('event/<int:pk>/update',
          EventUpdateView.as_view(),
          name='event-update'),
     path('event/<int:pk>/delete',
          EventDeleteView.as_view(),
          name='event-delete'),
     path('about/',
          views.about,
          name='event-about'),
     path('event/<int:pk>/itemslist_for_event',
          views.ItemslistForEvent,
          name='event-detail'),
]
