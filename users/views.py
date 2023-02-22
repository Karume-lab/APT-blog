from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from core.decorator import cls_login_required

class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'dashboard/pages/index.html'
    
class ProfileView(View):
    template_name = 'dashboard/pages/users-profile.html'
    
    @method_decorator(cls_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # Fixing method not allowed (ERROR 405)
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        gender = request.POST.get("gender")
        bio = request.POST.get("bio")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        twitter_url = request.POST.get("twitter_link")
        github_url = request.POST.get("github_link") 
        linkedin_url = request.POST.get("linkedin_link")
        memoryFile = request.FILES.get("profile_image")
        
        user = request.user
        profile = request.user.profile
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        profile.bio = bio
        profile.phone = phone
        profile.twitter_url = twitter_url
        profile.github_url = github_url
        profile.linkedin_url = linkedin_url
        profile.gender = gender
        profile.image = memoryFile
        
        user.save()
        profile.save()
        messages.success(request, "Profile updated successfully!")
        return render(request, self.template_name)