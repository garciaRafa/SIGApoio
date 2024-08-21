# Generated by Django 5.0.6 on 2024-08-21 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_reservamensal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipolocal',
            name='tipo',
            field=models.CharField(choices=[('SALA', 'Sala'), ('LAB', 'Laboratório'), ('AUD', 'Auditório')], max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
