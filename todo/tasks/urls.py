from django.urls import path

from .import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasklist, name = 'task-list'),
    path('yourname/<str:name>' , views.yourName , name = 'yourname'),
]
