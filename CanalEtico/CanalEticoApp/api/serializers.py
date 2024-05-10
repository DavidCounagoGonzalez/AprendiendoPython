from rest_framework.serializers import ModelSerializer
from CanalEticoApp.models import Comunicado, Tipo, Usuario
        
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellidos', 'relacion', 'email', 'telefono']
        
class TipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'tipo']
        
class ComunicadoSerializer(ModelSerializer):
    tipo = TipoSerializer()
    comunicante = UsuarioSerializer()
    
    class Meta:
        model = Comunicado
        fields = ['token', 'contraseña', 'implicados', 'descripcion', 'lugar', 'testigos', 'avisado', 'fecha', 'pruebas', 'solucionado', 'tipo', 'comunicante', 'solucion']