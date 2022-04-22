from django.shortcuts import render
from .models import Paciente
from rest_framework import viewsets
from .serializers import PacienteSerializer

# Create your views here.

class PacienteViewset(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


def home(request):        
    return render(request, 'app/home.html',)
    
def articulos(request):
    return render(request, 'app/articulos.html')


def contacto(request):
    return render(request, 'app/contacto.html')


def nosotros(request):
    return render(request, 'app/nosotros.html')