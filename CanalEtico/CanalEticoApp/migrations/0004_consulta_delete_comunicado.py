# Generated by Django 5.0.4 on 2024-04-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CanalEticoApp', '0003_comunicado_contraseña_comunicado_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=12, unique=True)),
                ('contraseña', models.CharField(max_length=200)),
                ('implicados', models.TextField(blank=True)),
                ('descripcion', models.TextField()),
                ('lugar', models.CharField(max_length=124)),
                ('testigos', models.TextField(blank=True)),
                ('avisado', models.BooleanField(blank=True)),
                ('pruebas', models.FileField(blank=True, null=True, upload_to='prueba/%Y/%m/%D/')),
            ],
        ),
        migrations.DeleteModel(
            name='Comunicado',
        ),
    ]
