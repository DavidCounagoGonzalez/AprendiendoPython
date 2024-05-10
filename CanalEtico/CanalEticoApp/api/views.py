from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from CanalEticoApp.models import Comunicado, Usuario, Tipo
from CanalEticoApp.api.serializers import ComunicadoSerializer, UsuarioSerializer, TipoSerializer

class ComunicadoApiViewSet(ModelViewSet):
    serializer_class = ComunicadoSerializer
    queryset = Comunicado.objects.all().order_by( 'solucionado', 'fecha')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['token']
    filterset_fields = {
        'token': ['contains']
    }
    
class UsuariosApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
class TipoApiViewSet(ModelViewSet):
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all()