# Generated by Django 5.0.4 on 2024-04-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CanalEticoApp', '0007_comunicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='solucionado',
            field=models.BooleanField(default=False),
        ),
    ]