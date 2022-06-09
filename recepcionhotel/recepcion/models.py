from django.db import models

class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    formadepago = models.CharField(max_length=100)

class PagoTarjeta(models.Model):
    numtarjeta = models.IntegerField(default=0)
    codseguridad = models.IntegerField(default=0)
    nombrepropietario = models.CharField(max_length=100)
    cuotas = models.IntegerField(default=0)
    valor = models.FloatField(default=0.0)

class Habitacion(models.Model):
    numhabitacion = models.IntegerField(default=0)
    tipohabitacion = models.CharField(max_length=100)
    canthuespedes = models.IntegerField(default=0)
    condicion = models.CharField(max_length=100)  


