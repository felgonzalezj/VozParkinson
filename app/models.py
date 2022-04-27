import email
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

opciones_autor = [
    [0, "Admin"],
    [1, "Staff"],
]

opciones_categoria = [
    [0, "Alimentacion"],
    [1, "Medicamentos"],
    [2, "Agenda Medica"],
    [3, "Fonoaudiologia"],
]

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    categoria = models.IntegerField(choices=opciones_categoria)
    autor = models.IntegerField(choices=opciones_autor)
    texto = models.TextField()
    imagen = models.ImageField(upload_to="publicacion", null=True)
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __int__(self) :
        return self.id_publicacion

class Tipo_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=50)
    codigo_tipo_usuario = models.IntegerField()
    descripcion_tipo_usuario = models.TextField()
    class Meta:
        verbose_name = "Tipo de usuario"
        verbose_name_plural = "Tipo de usuarios"

    def __str__(self) :
        return self.nombre_tipo_usuario


class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_tipo_user = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Profesional(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    id_tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT)
    rutprofesional = models.CharField(max_length=30)
    nombreprofesional = models.CharField(max_length=30)
    apellidopaternoprofesional = models.CharField(max_length=30)
    apellidomaternoprofesional = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=15)
    telegram = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return self.rutprofesional


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    rutpaciente = models.CharField(max_length=30)
    nombrepaciente = models.CharField(max_length=30)
    apellidopatpaciente = models.CharField(max_length=30)
    apellidomatpaciente = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30)
    telegram = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.rutpaciente


class Fonoaudiologo_paciente(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Id Usuario")
    idapp_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Rut Paciente")
    fecha = models.DateField()
    audio = models.FileField()
    video = models.FileField()
    feedback = models.TextField()
    class Meta:
        verbose_name = "Fonoaudiologo - Paciente"
        verbose_name_plural = "Fonoaudiologo - Paciente"

    def __str__(self):
        return self.nombrepaciente


class Paciente_Profesional(models.Model):
    id = models.AutoField(primary_key=True)
    idapp_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Rut Paciente")
    idapp_profesional = models.ForeignKey(Profesional, on_delete=models.PROTECT, verbose_name="Rut Profesional")
    id_tipo_usuario= models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT, verbose_name="Tipo usuario Profesional")
    class Meta:
        verbose_name = "Paciente - Profesional"
        verbose_name_plural = "Paciente - Profesional"

    def __int__(self):
        return self.id


class Enfermeria_paciente(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Id Usuario")
    idapp_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Rut Paciente")
    fecha_contactabilidad = models.DateField()
    bitacora_contactabilidad = models.TextField()
    class Meta:
        verbose_name = "Enfermeria - Paciente"
        verbose_name_plural = "Enfermeria - Paciente"

    def __int__(self):
        return self.id


class Medicamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombrelab = models.CharField(max_length=30, verbose_name="Nombre Laboratorio")
    nombremedicamen = models.CharField(max_length=30, verbose_name="Nombre Medicamento")
    dosismedicamento = models.CharField(max_length=40, verbose_name="Dosis Medicamento")
    cantidaddisplay = models.CharField(max_length=30, verbose_name="Cantidad Medicamento Display")
    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"

    def __str__(self):
        return self.nombremedicamen + ' / ' + self.nombrelab + ' / ' + self.dosismedicamento + ' / ' + self.cantidaddisplay


class MedicamentoCompra(models.Model):
    id = models.AutoField(primary_key=True)
    id_app_usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Id Usuario")
    idapp_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Rut Paciente")
    idapp_medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT, verbose_name="Medicamento/Laboratorio/Dosis/Cant.Display")
    fecha_compra = models.DateField()

    def __int__(self):
        return self.id

    