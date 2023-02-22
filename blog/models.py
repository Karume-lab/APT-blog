from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    status = models.CharField(choices=(("P", "published"), ("D", "draft")), max_length=1)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    published = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    slug = models.SlugField(db_index=True)
    
    def __str__(self):
        return (self.title)
    
    def __repr__(self):
        return (self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    active = models.BooleanField()
    comment = models.TextField()
    
    def __str__(self):
        return (f"{self.post}'s comment")