from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    return render(request, "core/index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(full_name = name, email = email, subject = subject, message = message)
        messages.success(request, "Thank you for you feedback!")
        return redirect('index')
        
    return render(request, "core/contact.html")

def about(request):
    return render(request, "core/about.html")
