from django.shortcuts import render, redirect
from .models import Persona

# Create your views here.

def mostrarPersona(request):
    personas = Persona.objects.all()
    return render(request, "mostrarPersona.html", {"personas": personas})

def creacionPersona(request):
    return render(request, "creacionPersona.html")

def crearPersona(request):
    identificacion = request.POST['txtIdentificacion']
    nombre = request.POST['txtNombre']
    edad = request.POST['numEdad']
    profesion = request.POST['txtProfesion']
    persona = Persona.objects.create(identificacion=identificacion, nombre=nombre, edad=edad, profesion=profesion)
    return redirect('/')

def actualizacionPersona(request, identificacion):
    persona = Persona.objects.get(identificacion=identificacion)
    return render(request, "actualizacionPersona.html", {"persona":persona})

def actualizarPersona(request):
    identificacion = request.POST['txtIdentificacion']
    nombre = request.POST['txtNombre']
    edad = request.POST['numEdad']
    profesion = request.POST['txtProfesion']

    persona = Persona.objects.get(identificacion=identificacion)
    persona.nombre = nombre
    persona.edad = edad
    persona.profesion = profesion
    persona.save()
    return redirect('/')


def eliminarPersona(request, identificacion):
    persona = Persona.objects.get(identificacion=identificacion)
    persona.delete()
    return redirect('/')


