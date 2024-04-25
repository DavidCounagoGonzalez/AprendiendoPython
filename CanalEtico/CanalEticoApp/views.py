from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, ComunicadoForm, ConsultaForm, SolucionForm
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Comunicado, Tipo
import secrets
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def consultar(request):
    if request.method == 'GET':
        return render(request, 'consultar.html', {'form': ConsultaForm})
    else:
        if Comunicado.objects.filter(token=request.POST['token']).count() > 0:
            contra = getHashPass(request.POST['token'])
            if check_password(request.POST['contraseña'], contra):
                request.session['tokenConsulta'] = request.POST['token']
                return redirect('revision')
            else:
                return render(request, 'consultar.html', {'form': ConsultaForm, 'error': 'Contraseña equivocada'})
        else:
            return render(request, 'consultar.html', {'form': ConsultaForm, 'error': 'NO existe ningún comunicado con ese código registrado'})


def getHashPass(codigo):
    contraseña_Com = Comunicado.objects.get(token=codigo)

    return contraseña_Com.contraseña


def revision(request):
    # try:
        data = Comunicado.objects.filter(
            token=request.session['tokenConsulta']).values()
        for x in data:
            del x['contraseña']
            x['tipo_id'] = Tipo.objects.get(id=x['tipo_id'])
        return render(request, 'revision.html', {'data': data})
    # except:
    #     return redirect('index')


def forma_comunicado(request):
    if request.method == 'GET':
        return render(request, 'ComForma.html')
    else:
        request.session['forma'] = request.POST['forma']
        if request.session['forma'] == '1':
            return redirect('userinfo')
        elif request.session['forma'] == '2':
            return redirect('comData')
        else:
            return render(request, 'ComForma.html', {
                'error': 'Ha ocurrido un error al realizar la acción'
            })


def verifica_User(post):
    error = ''

    cuenta = Usuario.objects.filter(email=post['email']).count()

    if cuenta >= 1:
        error = 'El email ya está registrado'
    else:
        error = 'Revise los datos indicados'
    return error


def get_IdUsuario(email):
    id_usuario = Usuario.objects.get(email=email)

    return id_usuario.id


def getEmailById(id_user):
    email_usuario = Usuario.objects.get(id=id_user)

    return email_usuario.email


def user_info(request):
    try:
        if request.session['forma'] != '1' and request.session['forma'] != '3':
            return redirect('forma')
        else:
            if request.method == 'GET':
                return render(request, 'InfoUser.html', {'form': UsuarioForm})
            else:
                form = UsuarioForm(request.POST)
                try:
                    error = verifica_User(request.POST)
                    new_User = form.save(commit=False)
                    new_User.save()
                    request.session['forma'] = request.POST['forma']
                    request.session['user'] = get_IdUsuario(
                        request.POST['email'])
                    return redirect('comData')
                except ValueError:
                    return render(request, 'InfoUser.html', {'form': UsuarioForm, 'error': error})
    except:
        return HttpResponse('No tienes permiso para acceder prueba a volver al <a href="/">inicio</a>', status=401)


def email_comunicante(request):
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
    try:
        if request.session['forma'] != '2' and request.session['forma'] != '3':
            return redirect('forma')
        else:
            if request.method == 'GET':
                return render(request, 'DataCom.html', {'form': ComunicadoForm})
            else:
                form = ComunicadoForm(request.POST)
                if form.is_valid():
                    if secrets.compare_digest(request.POST['contraseña'], request.POST['contraseña2']):
                        new_Com = form.save(commit=False)
                        new_Com.contraseña = make_password(
                            form.cleaned_data['contraseña'])
                        new_Com.token = secrets.token_hex(6)
                        request.session['token'] = new_Com.token
                        try:
                            new_Com.comunicante_id = request.session['user']
                        except:
                            pass

                        email_comunicante(request)
                        new_Com.save()
                        return redirect('finalizar')
                    else:
                        return render(request, 'DataCom.html', {'form': ComunicadoForm, 'error': 'Las contraseñas no coinciden'})
                else:

                    return render(request, 'DataCom.html', {'form': ComunicadoForm, 'error': 'revise los datos'})
    except:
        return HttpResponse('No tienes permiso para acceder prueba a volver al <a href="/">inicio</a>', status=401)


def finalizar(request):
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
