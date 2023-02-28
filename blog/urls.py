from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostList.as_view(), name='post_list'),
    # path('<slug:post_slug>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_details')
    path('<slug:post_slug>/<int:year>/<int:month>/<int:day>/', views.PostDetail.as_view(), name='post_detail'),
]
