from django.shortcuts import render
from .forms import UsuarioForm, ComunicadoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def consultar(request):
    return render(request, 'consultar.html', {'form': ComunicadoForm})