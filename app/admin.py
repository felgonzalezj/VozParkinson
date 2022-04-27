from django.contrib import admin
from .models import Tipo_Usuario , Account, Profesional, Publicacion, Paciente, Fonoaudiologo_paciente, Paciente_Profesional, Enfermeria_paciente, Medicamento, MedicamentoCompra
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline, )

class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre_tipo_usuario", "codigo_tipo_usuario", "descripcion_tipo_usuario"]

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ["id", "id_app_usuario", "id_tipo_usuario", "rutprofesional", "nombreprofesional","apellidopaternoprofesional", "email","telefono","whatsapp", "telegram"]

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["id_publicacion", "titulo", "fecha_publicacion", "categoria", "autor", "texto", "imagen"]

class FonoPacienteAdmin(admin.ModelAdmin):
    list_display = ["id_app_usuario", "idapp_paciente",   "fecha", "audio", "video","feedback"]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["id", "id_app_usuario", "rutpaciente", "nombrepaciente", "apellidopatpaciente", "email", "telefono","whatsapp","telegram"]

class Paciente_ProfesionalAdmin(admin.ModelAdmin):
    list_display = ["idapp_paciente","idapp_profesional", "id_tipo_usuario"]

class Enfermeria_pacienteAdmin(admin.ModelAdmin):
    list_display = ["id", "id_app_usuario","idapp_paciente","fecha_contactabilidad","bitacora_contactabilidad"]

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombrelab","nombremedicamen","dosismedicamento","cantidaddisplay"]

class MedicamentoCompraAdmin(admin.ModelAdmin):
    list_display = ["id_app_usuario","idapp_paciente" ,"idapp_medicamento", "fecha_compra"]

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Tipo_Usuario, Tipo_usuarioAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Fonoaudiologo_paciente, FonoPacienteAdmin)
admin.site.register(Paciente_Profesional, Paciente_ProfesionalAdmin)
admin.site.register(Enfermeria_paciente, Enfermeria_pacienteAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(MedicamentoCompra, MedicamentoCompraAdmin)
