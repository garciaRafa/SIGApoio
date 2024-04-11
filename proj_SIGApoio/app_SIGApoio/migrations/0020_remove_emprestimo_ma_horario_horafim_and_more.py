# Generated by Django 5.0.4 on 2024-04-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_SIGApoio', '0019_horario_dia_alter_emprestimo_ma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='ma',
        ),
        migrations.AddField(
            model_name='horario',
            name='horaFim',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='horaInicio',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
