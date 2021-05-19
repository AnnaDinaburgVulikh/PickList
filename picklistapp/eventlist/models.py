from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Invitees(models.Model):
    invitee = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.invitee


class Items_to_bring(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField

    def __str__(self):
        return self.name

class Items_for_invitees(models.Model):
    invitee = models.ForeignKey(Invitees, on_delete=models.CASCADE)
    item = models.ForeignKey(Items_to_bring, on_delete=models.CASCADE)
    amount = models.IntegerField
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.invitee