# Generated by Django 5.0.4 on 2024-04-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CanalEticoApp', '0009_comunicado_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='avisado',
            field=models.BooleanField(blank=True, choices=[('True', 'Si'), ('False', 'No'), ('', 'No lo sé')], default='False'),
        ),
    ]
