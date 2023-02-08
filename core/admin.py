from django.contrib import admin
from .views import Contact

#registering a model to the admin panel
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'message']