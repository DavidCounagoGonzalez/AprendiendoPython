from django.contrib import admin
from DatosAPI.models import Datos

# Register your models here.
@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    