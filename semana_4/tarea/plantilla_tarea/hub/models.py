# ============================================================
# SEMANA 4 — TAREA
#
# TAREA 1  → Lee el modelo Recurso ya definido
# TAREA 2 → Define el modelo Mensaje desde cero
# TAREA 3 → Registra ambos modelos en admin.py
#
# ENTREGA: models.py + admin.py funcionando.
# CRITERIO: Ambos modelos aparecen en http://127.0.0.1:8000/admin/
# ============================================================

from django.db import models


# Modelo ya dado — observa su estructura
class Recurso(models.Model):
    titulo      = models.CharField(max_length=200)
    url         = models.URLField()
    descripcion = models.TextField(blank=True)
    creado      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo


# ============================================================
# TAREA 2 — Define el modelo Mensaje
#
# El formulario de contacto necesita guardar:
#   - Nombre del remitente
#   - Correo electrónico
#   - El texto del mensaje
#   - La fecha y hora en que llegó (automática)
#   - Si el docente ya lo leyó (booleano, por defecto False)
#
# Prompt Cursor (Ctrl+K):
#   "Crea un modelo Django Mensaje con campos para guardar
#    mensajes de contacto: nombre, correo, mensaje, recibido
#    y leido. Sigue la misma estructura del modelo Recurso
#    de arriba."
# ============================================================

# ESCRIBE EL MODELO MENSAJE AQUÍ ↓
