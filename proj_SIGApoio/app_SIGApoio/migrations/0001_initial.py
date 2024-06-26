# Generated by Django 5.0.4 on 2024-04-04 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('tipo', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.BooleanField(blank=True, choices=[(True, 'Disponível'), (False, 'Indispovível')], default=True)),
                ('funcionando', models.BooleanField(blank=True, choices=[(True, 'Sim'), (False, 'Não')], default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_SIGApoio.tiporecurso')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_SIGApoio.tipousuario')),
            ],
        ),
    ]
