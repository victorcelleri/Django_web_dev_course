# ============================================================
# SEMANA 5 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa la zona de personalización
# EJERCICIO 2 → Completa la vista contacto()
#
# ENTREGA: Este archivo views.py con contacto() funcionando.
# CRITERIO: El formulario guarda mensajes y muestra confirmación.
# ============================================================

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recurso, Mensaje
from .forms import ContactoForm

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Química"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente
# ════════════════════════════════════════════════════════════


def inicio(request):
    return render(request, 'hub/inicio.html', {'nombre_docente': nombre_docente, 'materia': materia, 'institucion': institucion, 'frase_mision': frase_mision})


def acerca(request):
    return render(request, 'hub/acerca.html', {'nombre_docente': nombre_docente, 'materia': materia, 'institucion': institucion, 'anos_experiencia': anos_experiencia})


def recursos_view(request):
    return render(request, 'hub/recursos.html', {'nombre_docente': nombre_docente, 'recursos': Recurso.objects.all()})


# ============================================================
# EJERCICIO — Completa la vista contacto()
#
# Prompt Cursor (Ctrl+K):
#   "Crea la vista contacto() que maneje GET y POST.
#    En GET: instancia ContactoForm vacío y renderiza
#    'hub/contacto.html' con el formulario en el contexto.
#    En POST: valida el formulario; si es válido, crea un
#    Mensaje con los datos limpios, agrega messages.success
#    y redirige a 'contacto'. Si no es válido, re-renderiza
#    con el formulario y sus errores."
# ============================================================
def contacto(request):
    # COMPLETA AQUÍ ↓
    pass
