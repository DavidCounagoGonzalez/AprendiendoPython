from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolucionForm, TipoFiltro
from django.http import JsonResponse
from .models import Comunicado, Usuario, Tipo
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import requests
import environ
env = environ.Env()
environ.Env.read_env()

username = env('USUARIO_API')
contra = env('PASS_API')

def logueo(request):
    if request.user.is_authenticated: #Si el usuario ya está logueado lo redirige a la vista de los comunicados
        return redirect('listar')
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password']) #Comprobamos que los datos sean correctos

        if usuario is None: #Si no devolvemos la página con un error
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            
            login(request, usuario) #Si coinciden realizamos en login
            return redirect('listar')

def cerrar_sesion(request): #función para cerrar la sesión
    logout(request)
    return redirect('logueo')

def get_Comunicados(request):
    
    url_get = 'http://127.0.0.1:8000/api/comunicado/'
    response = requests.get(url_get, auth=(username, contra))
    
    if response.status_code == 200:
        data = response.json()

    # comunicados = Comunicado.objects.values() #Recogemos todos los comunicados
    # comunicados = list(comunicados.order_by( 'solucionado', 'fecha')) # Los ordenamos de manera ascendente primero los no solucionados y por fecha
    
    for comunicado in data['results']:
        del (comunicado['contraseña']) #Eliminamos la contraseña guardada en cada uno ya que no la queremos 
        comunicado['tipo'] = comunicado['tipo']['tipo'] #Recogemos la descripción coincidente al tipo de comunicado
        try:
            comunicado['comunicante'] = comunicado['comunicante']['nombre'] + ' ' + comunicado['comunicante']['apellidos'] #En caso de ser personal mostramos el nombre
        except:
            comunicado['comunicante'] = ''
     
    if (len(data['count'])>0):
        data = {'message': 'Success', 'comunicados': data['results']} #Si se han encontrado comunicados los devolvemos en forma de json
    else:
        data = {'message': 'No se encontraron'}
    
    return JsonResponse(data)
        
def gestion(request): #cargamos la vista de los comunicados con u  formulario para el select de tipos
    
    return render(request, 'gestion.html', {'form' : TipoFiltro })

def ver_comunicado(request, token):
      
    # comunicado = get_object_or_404(Comunicado, token=token) #Si no conseguimos un objeto Comunicado con el token pasado por url devolvemos un 404
    if request.method == 'GET':
        url_get = 'http://127.0.0.1:8000/api/comunicado/' + token + '/'
        response = requests.get(url_get, auth=(username, contra))
    
        if response.status_code == 200:
            data = response.json()
        
        data['tipo'] = data['tipo']['tipo']
        if data['comunicante']:
            data['comunicante'] = data['comunicante']['nombre'] + ' ' + data['comunicante']['apellidos']
        
        return render(request, 'ver_comunicado.html', {'comunicado': data, 'form': SolucionForm}) #cargamos el comunicado con sus datos y un textfield en caso de que este aún no tenga solución, en su defecto se mostrará esta.
    
    elif request.method == 'POST': #En caso de dar una solución se actualiza el comunicando dandole la solucióne escrita y pasando el estado a solucionado.
        url_change = 'http://127.0.0.1:8000/api/comunicadoCambios/' + token + '/'
        response = requests.get(url_change, auth=(username, contra))
    
        if response.status_code == 200:
            data = response.json()
            
        data['solucionado'] = True
        data['solucion'] = request.POST['solucion']
        
        if (data['comunicante']):
            id_user = data['comunicante']
            email_solucion(request, id_user, data['token'], data['solucion']) #Mandamos el email con el token del comunicado y su solución, en caso de que haya a quien enviarlo.
          
        # comunicado.save()
        res  = requests.put(url_change, data=data, auth=(username, contra))
        print(res)
        return redirect('listar')
    
def email_solucion(request, id_user, token, solucion): #Creamos la estructura y envio del email, con un try por si no existe el usuario.
    try:
        email = getEmailById(id_user) #Recogemos el email al que enviarlo mediante el id de usuario al que pertenece el comunicado
        asunto = 'Solucón a su comunicado'
        template = render_to_string('email.html', {
                                    'mensaje': solucion,
                                    'codigo': 'Este es el código de su comunicado: ' + token,
                                    'email': 'Desde el canal ético.'
                                })

        mail = EmailMessage(
                            asunto,
                            template,
                            settings.EMAIL_HOST_USER,
                            [email]
                            )

        mail.fail_silently = False
        mail.send()
    except:
        pass
    
def getEmailById(id_user): #Función para recoger el email mediante el id de usuario
    email_usuario = Usuario.objects.get(id=id_user)

    return email_usuario.email