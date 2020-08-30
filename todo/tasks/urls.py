from django.urls import path

from .import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.tasklist, name = 'task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('yourname/<str:name>' , views.yourName , name = 'yourname'),
]
