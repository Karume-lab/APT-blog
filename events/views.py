from django.shortcuts import render
from django.views.generic import ListView
from .models import Event

class EventList(ListView):
    template_name = "events/event_list"
    model = Event
    context_object_name = "events"