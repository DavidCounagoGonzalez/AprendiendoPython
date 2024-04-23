from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import datetime, date

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número debe tener el formatgo: '+999999999'. Hasta 15 dígitos es válido.")
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
class Tipo(models.Model):
    tipo = models.CharField(max_length=124, blank=True)
    
    def __str__(self):
        return self.tipo

class Comunicado(models.Model):
    class Avisado(models.TextChoices):
        SI = 'True', 'Si'
        NO = 'False', 'No'
        NS = 'None', 'No lo sé'
        
    TRUE_FALSE_CHOICES = (
        (True, 'Si'),
        (False, 'No')
    )
    
    token = models.CharField("Código del comunicado", max_length=12, unique=True)
    contraseña =  models.CharField(max_length=200, blank=False, validators=[MinLengthValidator(8)])
    tipo = models.ForeignKey(Tipo, default=1, on_delete=models.PROTECT)
    implicados = models.TextField(blank=True)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=124)
    testigos = models.TextField(blank=True)
    avisado = models.BooleanField("Algún superior fue avisado?", choices= TRUE_FALSE_CHOICES, default='', null=True)
    fecha = models.DateField(auto_now_add = True, blank=True)
    pruebas = models.FileField(blank=True, null=True, upload_to="prueba/%Y/%m/%D/")
    solucionado = models.BooleanField(default=False)
    comunicante = models.ForeignKey(Usuario, blank=True, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.token