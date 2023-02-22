from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status = "P")
    blogs = [post for post in posts]
    context = {
        "posts" : posts,
        "blogs" : blogs,
        }
    
    return render(request, "blog/post_list.html", context)

def post_detail(request, post_slug, title, year, month, day):
    post = get_object_or_404(Post, slug=post_slug, created__year=year, created__month=month, created__day=day)
    context = {
        "post": post,
        }
    
    return render(request,"blog/post_detail.html", context)