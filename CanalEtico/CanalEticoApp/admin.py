from django.contrib import admin
from .models import Comunicado, Usuario, Tipo

# Register your models here.

admin.site.register(Comunicado)
admin.site.register(Usuario)
admin.site.register(Tipo)