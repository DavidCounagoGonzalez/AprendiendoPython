from rest_framework.routers import DefaultRouter
from DatosAPI.api.views import DatosViewSet

router_datos = DefaultRouter()

router_datos.register(prefix='datos', basename='datos', viewset=DatosViewSet)