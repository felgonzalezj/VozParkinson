from dataclasses import fields
from .models import Paciente, Medicamento, MedicamentoCompra
from rest_framework import serializers


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['rutpaciente', 'nombrepaciente', 'apellidopatpaciente', 'email']

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['nombrelab', 'nombremedicamen', 'dosismedicamento', 'cantidaddisplay']

class MedCompSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentoCompra
        fields = ['idapp_paciente', 'idapp_medicamento', 'fecha_compra']