from dataclasses import fields
from .models import Paciente
from rest_framework import serializers


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['rutpaciente', 'nombrepaciente', 'apellidopatpaciente', 'email']
