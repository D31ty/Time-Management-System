#My coding
from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('create', views.createtodo, name="createtodo"),
    path('profile', views.profile, name="profile"),
    path('todo/<int:todo_pk>', views.viewtodo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name="completetodo"),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name="deletetodo"),
    path('', views.currenttodos, name="home"),
    path("completed", views.completedtodos, name="completedtodos"),
]