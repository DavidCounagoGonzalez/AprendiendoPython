from django.shortcuts import render
import urllib.request
import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
 
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def listar_todo(request):
    datos = {}
    if request.method == 'GET':
        url_api = urllib.request.Request('https://eldenring.fanapis.com/api/creatures')
        
        source = urllib.request.urlopen(url_api).read()
        
        lista_datos = json.loads(source)
        
        datos = lista_datos['data']
    else:
        datos = {}
        
    return render(request, 'todos.html', {'datos': datos})

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def logueo(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if usuario is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, usuario)
            return redirect('index')
        
def cerrar_sesion(request):
    logout(request)
    return redirect ('index')