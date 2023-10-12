from django.urls import path
from django.views.decorators.cache import cache_page

from app_blog.apps import AppBlogConfig
from app_blog.views import BlogListView, BlogDetailView

app_name = AppBlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    # path('article/<int:pk>/', BlogDetailView.as_view(), name='blog_article'),
    path('article/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_article'),

    # path('create/', BlogCreateView.as_view(), name='blog_create'),
    # path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    # path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
