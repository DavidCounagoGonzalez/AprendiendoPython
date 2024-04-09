from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.listar_todo, name='listar_todo'),
    path('login/', views.logueo, name='logueo'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('create/', views.registrar_criaturas, name='create')
]