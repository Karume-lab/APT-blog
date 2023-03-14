from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from blog.models import Post
from .serializers import PostSerlializer


class PostView(ListAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostSerlializer
