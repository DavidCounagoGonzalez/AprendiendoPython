from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número debe tener el formatgo: '+999999999'. Hasta 15 dígitos es válido.")
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True)

class Comunicado(models.Model):
    class Tipo(models.TextChoices):
        LEG = "1", "Incumplimiento de la legislación y/o normas internas"
        ACT = "2", "Actuación inadecuada, no ética, o falta de integridad en el desempeño profesional"
        TRA = "3", "Trato irrespetuoso, desigual o injusto"
        DIS = "4", "Discriminación o violación de los derechos humanos"
        VLC = "5", "Violencia, acoso o abuso"
        COR = "6", "Corrupción y/o fraude"
        BNQ = "7", "Conducta relacionada con el blanqueo de capitales"
        DMG = "8", "Daños contra el medio ambiente"
        SEG = "9", "Riesgos de seguridad y salud"
        ACC = '10', "Actos contra la libre competencia"
        INP = '11', "Infracción de la normativa de protección de datos"
        
    class Avisado(models.TextChoices):
        SI = 'True', 'Si'
        NO = 'False', 'No'
        NS = '', 'No lo sé'
    
    token = models.CharField("Código del comunicado", max_length=12, unique=True)
    contraseña =  models.CharField(max_length=200, blank=False, validators=[MinLengthValidator(8)])
    tipo = models.CharField(max_length=2, choices=Tipo.choices, default=Tipo.LEG)
    implicados = models.TextField(blank=True)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=124)
    testigos = models.TextField(blank=True)
    avisado = models.BooleanField("Algún superior fue avisado?", choices=Avisado.choices, default=Avisado.NO, null=True)
    fecha = models.DateTimeField(auto_now_add = True)
    pruebas = models.FileField(blank=True, null=True, upload_to="prueba/%Y/%m/%D/")
    solucionado = models.BooleanField(default=False)
    comunicante = models.ForeignKey(Usuario, blank=True, on_delete=models.PROTECT, default=0)