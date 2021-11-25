# Generated by Django 3.2.9 on 2021-11-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
            },
        ),
    ]