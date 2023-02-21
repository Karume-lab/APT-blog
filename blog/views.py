from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status = "D")
    context = {"post" : posts}
    
    return render(request, "blog/post_list.html", context)
