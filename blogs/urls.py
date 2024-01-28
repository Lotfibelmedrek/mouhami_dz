from django.urls import path
from .views import  BlogCreateView, BlogListView

urlpatterns = [
    path('blogs/create', BlogCreateView.as_view(), name='create-blog'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
]
