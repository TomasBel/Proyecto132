from django.db import models

class MiFamily(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fecha_nac = models.DateField()

class   estudiantes1(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    
class   profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    profesion = models.CharField(max_length=60)

class   entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaDeEntrega = models.DateField()

class   curso(models.Model):
    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()