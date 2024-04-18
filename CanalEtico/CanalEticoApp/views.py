from django.shortcuts import render, redirect
from .forms import UsuarioForm, ComunicadoForm, ConsultaForm
from django.http import HttpResponse
from .models import Usuario, Comunicado

# Create your views here.
def index(request):
    return render(request, 'index.html')

def consultar(request):
    return render(request, 'consultar.html', {'form': ConsultaForm})

def tipo_comunicado(request):
    if request.method == 'GET':
        return render(request, 'ComForma.html')
    else:
        request.session['tipo'] = request.POST['tipo']
        print(request.session['tipo'])
        if request.session['tipo'] == '1':
            return redirect('userinfo')
        elif request.session['tipo'] == '2':
            return redirect('comData')
        else:
            return render(request, 'ComForma.html', {
                'error': 'Ha ocurrido un error al realizar la acción'
            })
            
def verifica_User(post):
    error = ''
    
    cuenta = Usuario.objects.filter(email=post['email']).count()
    
    if cuenta >= 1:
        error = 'El email ya existe está registrado'
    else:
        error = 'Revise los datos indicados'
    return error

def get_IdUsuario(email):
    id_usuario = Usuario.objects.get(email=email)
    
    return id_usuario.id
            
def user_info(request):
    try:
        if request.session['tipo'] != '1' and request.session['tipo'] != '3':
            return redirect('tipo')
        else:
            if request.method == 'GET':
                return render(request, 'InfoUser.html', {'form': UsuarioForm})
            else:
                try:
                    form = UsuarioForm(request.POST)
                    error = verifica_User(request.POST)
                    new_User = form.save(commit=False)
                    new_User.save()
                    request.session['tipo'] = request.POST['tipo']
                    request.session['user']= get_IdUsuario(request.POST['email'])
                    return redirect('comData')
                except ValueError:
                    return render(request, 'InfoUser.html', {'form': UsuarioForm, 'error': error})
    except:
        return HttpResponse('No tienes permiso para acceder prueba a volver al <a href="/">inicio</a>', status=401)

def data_comunicado(request):
    print(request.session['tipo'])
    return render(request, 'DataCom.html', {'form': ComunicadoForm})

def finalizar(request):
    return render(request, 'final.html')