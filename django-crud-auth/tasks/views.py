from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


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
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def tasks(request):
    return render(request, 'tasks.html')

def create_task(request):
    
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        print(request.POST)
        return render(request, 'create_task.html', {
            'form': TaskForm
        })

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def loguearse(request):
    if request.method == "GET":
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
            return redirect('tasks') 
