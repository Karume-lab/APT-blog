from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Event(models.Model):
    title = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer')
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    description = models.TextField()
    status = models.CharField(choices=(("P", "physical"), ("V", "virtual"), ("B", "both")), max_length=1)
    venue = models.CharField(max_length=255)
    link = models.URLField(max_length=100)
    date = models.DateField()
    published = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(db_index=True)
    
    def get_absolute_url(self):
        return reverse("events:event_detail", args=(self.slug, self.published.year, self.published.month, self.published.day))
    
    def __str__(self) -> str:
        return self.title
    