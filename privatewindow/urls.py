from django.urls import path

from . import views

urlpatterns = [
    path('', views.privateWindow, name='privatewindow'),
    # path('<slug:slug>/', views.room, name='room'),
]