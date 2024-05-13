from rest_framework.serializers import ModelSerializer
from CanalEticoApp.models import Comunicado, Tipo, Usuario
        
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'
        
class ComunicadoSerializer(ModelSerializer):
    tipo = TipoSerializer()
    comunicante = UsuarioSerializer()
    
    class Meta:
        model = Comunicado
        fields = '__all__'
        
class ComunicadoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comunicado
        fields = '__all__'