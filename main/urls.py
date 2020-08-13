from django.urls import path

from main import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailsView.as_view(), name='post-details'),
    path('posts/create/', views.CreatePostView.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', views.UpdatePostView.as_view(), name='update-post'),
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
]