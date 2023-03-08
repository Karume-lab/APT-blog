from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 
                    'organizer', 
                    'image', 
                    'description', 
                    'status', 
                    'venue', 
                    'link', 
                    'date', 
                    'published', 
                    'slug'
                    ]
    
    prepopulated_fields = {
        "slug":('title',),
            }