from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('createroom/create/', views.createRoom, name='room'),
    path('<slug:slug>/', views.room, name='room'),
]