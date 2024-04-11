from django.shortcuts import render
import urllib.request
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Creatures
from django.core.paginator import Paginator
from django.http import Http404
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def recoger_datos(url):
    datos = []
    for page in range(5):
        url_api = urllib.request.Request(str(url) + str(page))

        source = urllib.request.urlopen(url_api).read()

        lista_datos = json.loads(source)

        datos = datos + lista_datos['data']

    return datos


def registrar_criaturas(request):
    datos = recoger_datos(
        'https://eldenring.fanapis.com/api/creatures?limit=100&page=')

    criatura = Creatures()

    for dato in datos:

        criatura.id = dato['id']
        criatura.name = dato['name']
        criatura.image = dato['image']
        criatura.description = dato['description']
        try:
            criatura.location = dato['location']
            criatura.drops = dato['drops']
        except KeyError:
            print('No sé porqué salta pero ta weno')
        criatura.save()
    return render(request, 'create.html')


@login_required
def listar_todo(request):
    criaturas = Creatures.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(criaturas, 18)
        criaturas = paginator.page(page)
    except:
        raise Http404

    return render(request, 'todos.html', {'criaturas': criaturas, 'paginator': paginator})


def signup(request):
    data = {
        'form':  CustomUserCreationForm
    }
    if request.method == "POST":
        usuario_form = CustomUserCreationForm(data=request.POST)
        # registrar usuario
        if usuario_form.is_valid():
            usuario_form.save()
            usuario = authenticate(
                username=usuario_form.cleaned_data['username'], password=usuario_form.cleaned_data['password1'])
            login(request, usuario)
            return redirect('index')
        else:
            data['error'] = 'Comprueba que las credenciales cumplan los requisitos'
    return render(request, 'signup.html', data)


def logueo(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

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
    return redirect('index')

