from django.urls import path, re_path
from . import views

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/', views.consultar, name='consultar'),
    path('comunicacion/tipo/' ,views.tipo_comunicado, name='tipo'),
    path('comunicacion/user/', views.user_info, name='userinfo'),
    path('comunicacion/registro/', views.data_comunicado, name='comData'),
    path('comunicacion/finalizar/', views.finalizar, name='finalizar')
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',
            serve, {
                'document_root': settings.MEDIA_ROOT,
            }),
    ]