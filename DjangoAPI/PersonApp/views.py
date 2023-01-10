from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PersonApp.models import Profesiones, Personas
from PersonApp.serializers import PersonaSerializer, ProfesionSerializer

# Create your views here.

@csrf_exempt
def mostrarProfesion(request):
    if request.method=='GET':
        profesiones = Profesiones.objects.all()
        profesiones_serializer = ProfesionSerializer(profesiones, many=True)
        return JsonResponse(profesiones_serializer.data, safe=False)

@csrf_exempt
def crearProfesion(request):
    if request.method=='POST':
        profesion_data = JSONParser().parse(request)
        profesion_serializer = ProfesionSerializer(data=profesion_data)
        if profesion_serializer.is_valid():
            profesion_serializer.save()
            return JsonResponse("Creación Exitosamente!!!", safe=False)
        return JsonResponse("Fallo al Crear.", safe=False)

@csrf_exempt
def actualizarProfesion(request):
    if request.method == 'POST':
        profesion_data = JSONParser().parse(request)
        profesion = Profesiones.objects.get(Id=profesion_data['Id'])
        profesion_serializer = ProfesionSerializer(profesion, data=profesion_data)
        if profesion_serializer.is_valid():
            profesion_serializer.save()
            return JsonResponse("Actualización Exitosamente!!!", safe=False)
        return JsonResponse("Fallo al Actualizar.", safe=False)

@csrf_exempt
def eliminarProfesion(request, id):
    if request.method == 'DELETE':
        profesion = Profesiones.objects.get(Id=id)
        profesion.delete()
        return JsonResponse("Eliminación Exitosamente!!!", safe=False)


#------PERSONA-------   

@csrf_exempt
def mostrarPersona(request):
    if request.method=='GET':
        personas = Personas.objects.all()
        personas_serializer = PersonaSerializer(personas, many=True)
        return JsonResponse(personas_serializer.data, safe=False)

@csrf_exempt
def crearPersona(request):
    if request.method=='POST':
        persona_data = JSONParser().parse(request)
        persona_serializer = PersonaSerializer(data=persona_data)
        if  persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Creación Exitosamente!!!", safe=False)
        return JsonResponse("Fallo al Crear.", safe=False)

@csrf_exempt
def actualizarPersona(request):
    if request.method == 'POST':
        persona_data = JSONParser().parse(request)
        persona = Personas.objects.get(Id=persona_data['Id'])
        persona_serializer = PersonaSerializer(persona, data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Actualización Exitosamente!!!", safe=False)
        return JsonResponse("Fallo al Actualizar.", safe=False)

@csrf_exempt
def eliminarPersona(request, id):
    if request.method == 'DELETE':
        persona = Personas.objects.get(Id=id)
        persona.delete()
        return JsonResponse("Eliminación Exitosamente!!!", safe=False)