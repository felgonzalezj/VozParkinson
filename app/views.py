from django.shortcuts import render
from .models import Medicamento, MedicamentoCompra, Paciente, Publicacion
from rest_framework import viewsets
from .serializers import PacienteSerializer, MedicamentoSerializer, MedCompSerializer

# Create your views here.

class PacienteViewset(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicamentoViewset(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedCompViewset(viewsets.ModelViewSet):
    queryset = MedicamentoCompra.objects.all()
    serializer_class = MedCompSerializer


def home(request):        
    return render(request, 'app/home.html',)
    
def articulos(request):
    publicacion = Publicacion.objects.all()
    data = {
        'Publicacion' : publicacion
    }
    return render(request, 'app/articulos.html', data)


def contacto(request):
    return render(request, 'app/contacto.html')


def nosotros(request):
    return render(request, 'app/nosotros.html')