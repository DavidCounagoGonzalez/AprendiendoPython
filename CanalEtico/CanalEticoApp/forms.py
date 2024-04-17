from django.forms import ModelForm
from django import forms
from .models import Usuario, Comunicado

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'relacion', 'email', 'telefono']
        
class ComunicadoForm(ModelForm):
    
    class Meta:
        model = Comunicado
        fields = ['tipo', 'descripcion', 'implicados', 'lugar', 'testigos', 'avisado', 'pruebas', 'contraseña', 'contraseña' ]