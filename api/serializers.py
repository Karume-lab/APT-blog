from rest_framework import serializers
from blog.models import Post

class PostSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title","author", "status", "body", "image",)