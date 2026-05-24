from django.contrib import admin
from .models import Recurso, Mensaje


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'url', 'creado']
    search_fields = ['titulo', 'descripcion']


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display   = ['nombre', 'correo', 'recibido', 'leido']
    list_filter    = ['leido']
    list_editable  = ['leido']
    readonly_fields = ['nombre', 'correo', 'mensaje', 'recibido']
