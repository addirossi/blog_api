from django.urls import path

from main.views import posts_list

urlpatterns = [
    path('posts/', posts_list, name='posts-list'),
]