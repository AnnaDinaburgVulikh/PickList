from django.apps import AppConfig


class EventlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventlist'


class Items_to_bringConfig(AppConfig):
    name = 'itemlist_for_event'
