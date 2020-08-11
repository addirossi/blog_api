from django.urls import path

from main.views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello-view')
]