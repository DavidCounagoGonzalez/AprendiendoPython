from django.shortcuts import render, redirect
from .forms import UsuarioForm, ComunicadoForm, ConsultaForm
from django.http import HttpResponse
from .models import Usuario, Comunicado, Tipo
import secrets
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import requests
import environ

env = environ.Env()
environ.Env.read_env()

username = env('USUARIO_API')
contra = env('PASS_API')


def index(request):
    return render(request, 'index.html')


def consultar(request):
    if request.method == 'GET': # En caso de la request sea de tipo GET se cargará la págian con el formulario
        return render(request, 'consultar.html', {'form': ConsultaForm})
    else:
        if Comunicado.objects.filter(token=request.POST['token']).count() > 0: #En caso de POST primero se comprobará si el token existe en la BBDD
            contra = getHashPass(request.POST['token']) #Se recoge la contraseña de dicho token  
            if check_password(request.POST['contraseña'], contra): #Se comparan ambas 
                request.session['tokenConsulta'] = request.POST['token'] # En caso de ser correcto se guarda el token en una session para cargar los datos a posterior.
                return redirect('revision') #Se redireje al usuario a la página para ver la información de su comunicado
            else:
                return render(request, 'consultar.html', {'form': ConsultaForm, 'error': 'Contraseña equivocada'})
        else:
            return render(request, 'consultar.html', {'form': ConsultaForm, 'error': 'NO existe ningún comunicado con ese código registrado'})


def getHashPass(codigo):
    contraseña_Com = Comunicado.objects.get(token=codigo) #Consulta a la BBDD para recoger la contraseña por token

    return contraseña_Com.contraseña


def revision(request):
    try:
        data = Comunicado.objects.filter(
            token=request.session['tokenConsulta']).values() #Recojo los datos del token solicitado
        for x in data:
            del x['contraseña'] #Elimino la contraseña de la lista
            x['tipo_id'] = Tipo.objects.get(id=x['tipo_id']) #Muestro la descripción del tipo de comunicado
        return render(request, 'revision.html', {'data': data})
    except:
        return redirect('index')


def forma_comunicado(request):
    if request.method == 'GET':
        return render(request, 'ComForma.html')
    else:
        request.session['forma'] = request.POST['forma']
        if request.session['forma'] == '1': # Si la opción ha sido personal devolverá 1 
            return redirect('userinfo')
        elif request.session['forma'] == '2': # Si la opción ha sido anónima devolverá 2 
            return redirect('comData')
        else:
            return render(request, 'ComForma.html', {
                'error': 'Ha ocurrido un error al realizar la acción'
            })


def verifica_User(post): #Esta función verifica que no exista un mismo correo en varios usuarios
    error = ''

    cuenta = Usuario.objects.filter(email=post['email']).count()

    if cuenta >= 1:
        error = 'El email ya está registrado'
    else:
        error = 'Revise los datos indicados'
    return error


def get_IdUsuario(email): #Esta función recoge el id de usuario mediante el email
    id_usuario = Usuario.objects.get(email=email)

    return id_usuario.id


def getEmailById(id_user): #Esta función recoge el email medianre el id de usuario
    email_usuario = Usuario.objects.get(id=id_user)

    return email_usuario.email

def user_info(request):
    # try:
        if request.session['forma'] != '1' and request.session['forma'] != '3': # Si elvalor de forma no es 1 o 3 quiere decir que el usuario no ha escogido personal, y no ha pasado por aquí
            return redirect('forma')
        else:
            if request.method == 'GET':
                return render(request, 'InfoUser.html', {'form': UsuarioForm})
            else:
                # form = UsuarioForm(request.POST)
                try:
                    error = verifica_User(request.POST) #Lanzamos la función para comprobar el correo
                    
                    # form.save() #Guardamos los datos pero sin escribirlos por el momento
                    
                    data = {
                        'nombre' : request.POST['nombre'],
                        'apellidos' : request.POST['apellidos'],
                        'relacion' : request.POST['relacion'],
                        'email' : request.POST['email'],
                        'telefono' : request.POST['telefono']
                    }
                    
                    print(request.POST['email'])
                    response = requests.post('http://127.0.0.1:8000/api/usuario/', data=data, auth=(username, contra))
                    request.session['forma'] = request.POST['forma'] #Pasamos el valor a 3 para que pueda acceder al siguiente form
                    request.session['user'] = get_IdUsuario(
                        request.POST['email'])
                    
                    if response.status_code == 201:
                        return redirect('comData')
                except ValueError:
                    return render(request, 'InfoUser.html', {'form': UsuarioForm, 'error': error})
    # except:
    #     return HttpResponse('No tienes permiso para acceder prueba a volver al <a href="/">inicio</a>', status=401)

def email_comunicante(request): #Función que redacta la estructura que tendrá el email y realiza el envio.
    try:
        email = getEmailById(request.session['user'])
        asunto = 'Código comunicado'
        template = render_to_string('email.html', {
                                    'mensaje': 'A continuación puede ver el código de su comunicado, recuerde que para acceder a él debe dirigirse al apartado de consulta e inidcar también la contraseña que indicó en el formulario',
                                    'codigo': request.session['token'],
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

def data_comunicado(request):
    # try:
        if request.session['forma'] != '2' and request.session['forma'] != '3': #Se puede acceder que con 2 en caso de seleccionar anoónimo o 3 si vienes de hacer el personal
            return redirect('forma')
        else:
            if request.method == 'GET':
                return render(request, 'DataCom.html', {'form': ComunicadoForm})
            else:
                form = ComunicadoForm(request.POST, request.FILES) #Recogemos tanto valores como archivos de los input
                if form.is_valid():
                    if secrets.compare_digest(request.POST['contraseña'], request.POST['contraseña2']): #Comprobamos que las contraseñas coinciden
                        new_Com = form.save(commit=False)
                        new_Com.contraseña = make_password(
                            form.cleaned_data['contraseña']) #hasheamos la contraseña
                        new_Com.token = secrets.token_hex(6) #Generamos el token para el comunicado
                        request.session['token'] = new_Com.token
                        
                        print(form.cleaned_data['pruebas'])
                        
                        try:
                            new_Com.comunicante_id = request.session['user'] #SI existe el id de usuario lo añadimos al objeto
                        except:
                            pass
                        
                        if 'pruebas' in request.FILES:
                            archivos = {
                                'pruebas' : (request.FILES['pruebas'].name, request.FILES['pruebas'], request.FILES['pruebas'].content_type)
                            }
                            
                        else:
                            archivos = None
                            
                        tipo = request.POST['tipo']
                        
                        data = {
                            'token': new_Com.token,
                            'contraseña': new_Com.contraseña,
                            'implicados': new_Com.implicados,
                            'descripcion': new_Com.descripcion,
                            'lugar': new_Com.lugar,
                            'testigos': new_Com.testigos,
                            'avisado': new_Com.avisado,
                            'tipo': tipo,
                            'comunicante': new_Com.comunicante_id or '',
                        }
                        email_comunicante(request) #Enviamos el email
                        
                        response = requests.post('http://127.0.0.1:8000/api/comunicadoCambios/', data=data, files=archivos, auth=(username, contra))
                        # new_Com.save() #Guardamos el objeto en la bbdd
                        if response.status_code == 201:
                            return redirect('finalizar')
                        else:
                            return render(request, 'DataCom.html', {'form': ComunicadoForm, 'error': 'Error al crear'})
                    else:
                        return render(request, 'DataCom.html', {'form': ComunicadoForm, 'error': 'Las contraseñas no coinciden'})
                else:

                    return render(request, 'DataCom.html', {'form': ComunicadoForm, 'error': 'revise los datos'})
    # except:
    #     return HttpResponse('No tienes permiso para acceder, prueba a volver al <a href="/">inicio</a>', status=401)

def finalizar(request):#Tratamos de borrar los datos de sesión y finalmente mostramos una página con el código del comunicado.
    try:
        del request.session['user']
        del request.session['forma']
    except:
        pass
    try:
        codigo = request.session['token']
        del request.session['token']
    except:
        return HttpResponse('Ha ocurrido un error, prueba a volver al <a href="/">inicio</a>', status=404)

    return render(request, 'final.html', {'codigo': codigo})
