from django.urls import path
from . import views

# Aquí se indican las urls de nuestra app web y su estructura
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:id>', views.project_details, name='project_details'),
    # path('tasks/<int:id>', views.tasks),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
]
