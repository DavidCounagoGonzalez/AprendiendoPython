from django.forms import ModelForm
from django import forms
from .models import Usuario, Comunicado
from django.core.validators import MinLengthValidator

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'relacion', 'email', 'telefono']
        
class ComunicadoForm(ModelForm):
    
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    contraseña2 = forms.CharField(label="Repite la Contraseña", max_length=200, validators=[MinLengthValidator(8)], widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = Comunicado
        fields = ['tipo', 'descripcion', 'implicados', 'lugar', 'testigos', 'avisado', 'pruebas', 'contraseña', 'contraseña2' ]
        
class ConsultaForm(ModelForm):
    
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    
    class Meta:
        model = Comunicado
        fields = ['token', 'contraseña']