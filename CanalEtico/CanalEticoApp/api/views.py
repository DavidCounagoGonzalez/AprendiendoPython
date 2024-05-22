from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from CanalEticoApp.models import Comunicado, Usuario, Tipo
from CanalEticoApp.api.serializers import ComunicadoSerializer, UsuarioSerializer, TipoSerializer, ComunicadoUpdateSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size = 25  # Número de elementos por página
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Límite máximo de elementos por página

class ComunicadoApiViewSet(ModelViewSet):
    serializer_class = ComunicadoSerializer
    queryset = Comunicado.objects.all().order_by( 'solucionado', 'fecha')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
                        'token': ['icontains']
                        }
    lookup_field = 'token'
    pagination_class = CustomPagination
    
class ComunicadoUpdateApiViewSet(ModelViewSet):
    serializer_class = ComunicadoUpdateSerializer
    queryset = Comunicado.objects.all().order_by( 'solucionado', 'fecha')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['token']
    lookup_field = 'token'
    parser_classes = (MultiPartParser, FormParser)
    
    
class UsuariosApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
class TipoApiViewSet(ModelViewSet):
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all()