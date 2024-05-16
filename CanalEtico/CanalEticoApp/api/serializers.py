from rest_framework.serializers import ModelSerializer
from CanalEticoApp.models import Comunicado, Tipo, Usuario
from rest_framework import serializers
        
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
    pruebas = serializers.FileField(required=False)  # Para archivos genéricos
    
    class Meta:
        model = Comunicado
        fields = '__all__'
        
    def save(self, **kwargs):
        print('Hola')
        # Extrae el archivo de los datos validados
        pruebas = self.validated_data.pop('pruebas', None)  # O 'imagen' según sea necesario

        # Crea una instancia de Comunicado con los datos validados
        comunicado = super().save(**kwargs)

        # Si se proporciona un archivo, guárdalo en la instancia de Comunicado
        if pruebas:
            comunicado.pruebas = pruebas  # O 'imagen' según sea necesario
            comunicado.save(update_fields=['pruebas'])

        return comunicado