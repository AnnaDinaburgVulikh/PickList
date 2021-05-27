from django.contrib import admin
from .models import Event, Invitees, Items_to_bring, Items_for_invitees

admin.site.register(Event)
admin.site.register(Invitees)
admin.site.register(Items_to_bring)
admin.site.register(Items_for_invitees)




