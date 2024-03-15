from django.urls import path

from . import views

urlpatterns = [
    path('', views.privateWindow, name='privatewindow'),
    path('<str:frndname>/', views.chatroom, name='chatroom'),
]