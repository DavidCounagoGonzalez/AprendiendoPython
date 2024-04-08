from django.db import models

# Create your models here.
class Datos(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()