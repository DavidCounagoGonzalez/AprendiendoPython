from django.urls import path
from . import views

urlpatterns = [
    path('all/<int:pagina>', views.index, name='index')
]