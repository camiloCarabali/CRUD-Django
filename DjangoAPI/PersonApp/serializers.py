from rest_framework import serializers
from PersonApp.models import Personas, Profesiones

class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesiones
        fields = ('Id', 'Nombre')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('Id', 'Identificacion', 'Nombre', 'Edad', 'Profesion')