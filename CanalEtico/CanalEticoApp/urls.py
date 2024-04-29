from django.urls import path, re_path
from . import views, viewsAdmin

from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/iniciar/', views.consultar, name='consultar'),
    path('consultar/revisar/', views.revision, name='revision'),
    path('comunicacion/forma/' ,views.forma_comunicado, name='forma'),
    path('comunicacion/user/', views.user_info, name='userinfo'),
    path('comunicacion/registro/', views.data_comunicado, name='comData'),
    path('comunicacion/finalizar/', views.finalizar, name='finalizar'),
    path('gestion/login/', viewsAdmin.logueo, name='logueo'),
    path('logout/', viewsAdmin.cerrar_sesion, name='logout'),
    path('gestion/listar/', login_required(viewsAdmin.get_Comunicados), name='gestion'),
    path('gestion/comunicados/', login_required(viewsAdmin.gestion), name='listar'),
    path('gestion/comunicados/<str:token>', login_required(viewsAdmin.ver_comunicado), name='verCom')
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',
            serve, {
                'document_root': settings.MEDIA_ROOT,
            }),
    ]