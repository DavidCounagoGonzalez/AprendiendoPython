from rest_framework.routers import DefaultRouter
from CanalEticoApp.api.views import ComunicadoApiViewSet, UsuariosApiViewSet, TipoApiViewSet, ComunicadoUpdateApiViewSet
from django.urls import path, include
  
  
router_comunicados = DefaultRouter()

router_comunicados.register(r'comunicado', ComunicadoApiViewSet)

router_comunicados.register('usuario', UsuariosApiViewSet)

router_comunicados.register('tipo', TipoApiViewSet)

router_comunicados.register(r'comunicadoCambios', ComunicadoUpdateApiViewSet, basename='comunicadoCambios')

urlpatterns = [
    path('', include(router_comunicados.urls))
]