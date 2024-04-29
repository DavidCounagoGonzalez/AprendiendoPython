from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolucionForm, TipoFiltro
from django.http import JsonResponse
from .models import Comunicado, Usuario, Tipo
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def logueo(request):
    if request.user.is_authenticated:
        return redirect('listar')
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if usuario is None:
            print('HOla')
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            
            login(request, usuario)
            return redirect('listar')

def cerrar_sesion(request):
    logout(request)
    return redirect('logueo')

def get_Comunicados(request):
    comunicados = Comunicado.objects.values()
    comunicados = list(comunicados.order_by( 'solucionado', 'fecha'))
    
    for comunicado in comunicados:
        del (comunicado['contraseña'])
        comunicado['tipo_id'] = Tipo.__str__(Tipo.objects.get(id=comunicado['tipo_id']))
        try:
            comunicado['comunicante_id'] = Usuario.__str__(Usuario.objects.get(id=comunicado['comunicante_id']))
        except:
            comunicado['comunicante_id'] = ''
     
    if (len(comunicados)>0):
        data = {'message': 'Success', 'comunicados': comunicados}
    else:
        data = {'message': 'No se encontraron'}
    
    return JsonResponse(data)
        
def gestion(request):
    
    
    return render(request, 'gestion.html', {'form' : TipoFiltro })

def ver_comunicado(request, token):
    comunicado = get_object_or_404(Comunicado, token=token)
    if request.method == 'GET':
        return render(request, 'ver_comunicado.html', {'comunicado': comunicado, 'form': SolucionForm})
    else:
        comunicado.solucion = request.POST['solucion']
        comunicado.solucionado = True
        
        id_user = comunicado.comunicante_id
        
        email_solucion(request, id_user, comunicado.token, comunicado.solucion)
        comunicado.save()
        return redirect('listar')
    
def email_solucion(request, id_user, token, solucion):
    try:
        email = getEmailById(id_user)
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
    
def getEmailById(id_user):
    email_usuario = Usuario.objects.get(id=id_user)

    return email_usuario.email