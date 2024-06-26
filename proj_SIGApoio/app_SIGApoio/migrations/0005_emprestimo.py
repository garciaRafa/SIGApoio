# Generated by Django 5.0.4 on 2024-04-05 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_SIGApoio', '0004_alter_usuario_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('horaSaida', models.DateTimeField()),
                ('horaEntrada', models.DateTimeField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('idRecurso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_SIGApoio.recurso')),
                ('matBolsista', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='app_SIGApoio.usuario')),
            ],
        ),
    ]
