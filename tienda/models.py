from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=9, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)