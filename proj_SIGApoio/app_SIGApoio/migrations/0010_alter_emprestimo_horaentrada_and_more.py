# Generated by Django 5.0.4 on 2024-04-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_SIGApoio', '0009_sala'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='horaEntrada',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='horaSaida',
            field=models.DateTimeField(auto_now=True),
        ),
    ]