# Generated by Django 4.0.4 on 2022-06-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numhabitacion', models.IntegerField(default=0)),
                ('tipohabitacion', models.CharField(max_length=100)),
                ('canthuespedes', models.IntegerField(default=0)),
                ('condicion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('documento', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100)),
                ('formadepago', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PagoTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numtarjeta', models.IntegerField(default=0)),
                ('codseguridad', models.IntegerField(default=0)),
                ('nombrepropietario', models.CharField(max_length=100)),
                ('cuotas', models.IntegerField(default=0)),
                ('valor', models.FloatField(default=0.0)),
            ],
        ),
    ]
