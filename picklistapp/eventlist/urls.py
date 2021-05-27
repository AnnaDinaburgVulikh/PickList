from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about/', views.about, name='event-about'),
    path('register/', views.about, name='register'),
]