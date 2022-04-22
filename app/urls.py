from django.urls import path, include
from .views import home, articulos, contacto, nosotros, PacienteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paciente', PacienteViewset)

urlpatterns = [
    path('', home, name="home"),

    path('articulo/', articulos, name="articulos"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('21292120194393482/', include(router.urls)),
]