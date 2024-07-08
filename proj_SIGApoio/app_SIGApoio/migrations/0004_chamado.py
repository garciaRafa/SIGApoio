# Generated by Django 5.0.4 on 2024-07-03 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_SIGApoio', '0003_alter_recurso_id_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id_chamado', models.IntegerField(primary_key=True, serialize=False)),
                ('chamado', models.CharField(max_length=200)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_SIGApoio.reserva')),
            ],
        ),
    ]
