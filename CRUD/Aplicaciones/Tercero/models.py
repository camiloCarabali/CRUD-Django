from django.db import models

# Create your models here.

class Persona(models.Model):

    class Profesion(models.TextChoices):
        INDETERMINADO = 'INDETERMINADO'
        DESEMPLEADO = 'DESEMPLEADO'
        EMPLEADO = 'EMPLEADO'
        PENSIONADO = 'PENSIONADO'

    identificacion = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField()
    profesion = models.CharField(choices=Profesion.choices, max_length=200)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.identificacion)