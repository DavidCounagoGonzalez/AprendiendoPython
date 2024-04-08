from rest_framework.viewsets import ModelViewSet
from DatosAPI.models import Datos
from DatosAPI.api.serializers import DatosSerializer

class DatosViewSet(ModelViewSet):
    serializer_class = DatosSerializer
    queryset = Datos.objects.all()