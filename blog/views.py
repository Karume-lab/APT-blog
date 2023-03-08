from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

def post_list(request):
    posts = Post.objects.filter(status = "P")
    blogs = [post for post in posts]
    context = {
        "posts" : posts,
        "blogs" : blogs,
        }
    
    return render(request, "blog/post_list.html", context)

def post_detail(request, post_slug, year, month, day):
    post = get_object_or_404(Post, slug=post_slug, created__year=year, created__month=month, created__day=day)
    context = {
        "post": post,
        }
    
    return render(request,"blog/post_detail.html", context)

class PostList(ListView):
    template_name = "blog/post_list.html"
    queryset = Post.objects.filter(status = "P")

class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status = "P")
    
    def get_object(self):
        return get_object_or_404(
            Post,
            slug=self.kwargs.get("post_slug"),
            created__year=self.kwargs.get("year"),
            created__month=self.kwargs.get("month"), 
            created__day=self.kwargs.get("day"))
    
    def post(self, request,post_slug, year, month, day):
        form = CommentForm(data=request.POST)
        
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.author = request.user
            new_comment.post=get_object_or_404(Post, 
                                               slug=post_slug, 
                                               created__year=year, 
                                               created__month=month, 
                                               created__day=day)
            new_comment.save()
            
        return redirect(reverse("blog:post_detail", args = [post_slug, year, month, day]))
    
                                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "form": CommentForm(),
            "post": self.get_object(),
        }
        return context
class MyPosts(LoginRequiredMixin, View):
    template_name = "blog/my_posts.html"
    
    def get(self, request, status=None):
        posts = Post.objects.filter(author=request.user)
        if status:
            posts = posts.filter(status=status[0].upper())
        context = {
            "posts":posts,
        }
        return render (request, self.template_name, context)