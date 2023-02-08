from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(null = True, blank = True)
    gender = models.CharField(choices=(("M", "male"), ("F", "female")), max_length=1, null=True, blank=True)
    phone = PhoneNumberField(null = True, blank=True)
    bio = models.TextField(max_length=255, null = True, blank = True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        