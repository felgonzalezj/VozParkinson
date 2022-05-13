from django.urls import path, include
from .views import home, articulos, contacto, pacientes, nosotros, PacienteViewset, MedicamentoViewset, MedCompViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paciente', PacienteViewset)
router.register('medicamento', MedicamentoViewset)
router.register('medicamentocompra', MedCompViewset)

urlpatterns = [
    path('', home, name="home"),

    path('articulo/', articulos, name="articulos"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('pacientes/', pacientes, name="pacientes"),
    path('21292120194393482/', include(router.urls)),
]