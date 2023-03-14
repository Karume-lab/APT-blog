from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('posts/', views.PostView.as_view(), name='post-api')
]
