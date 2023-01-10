from django.db import models

# Create your models here.

class Profesiones(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)

class Personas(models.Model):
    Id = models.AutoField(primary_key=True)
    Identificacion = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    Edad = models.PositiveIntegerField()
    Profesion = models.CharField(max_length=200)
