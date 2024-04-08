from rest_framework.serializers import ModelSerializer
from DatosAPI.models import Datos

class DatosSerializer(ModelSerializer):
    class Meta:
        model = Datos
        fields = ['id' , 'titulo', 'descripcion']
