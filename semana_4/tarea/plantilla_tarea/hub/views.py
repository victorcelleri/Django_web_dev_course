# ============================================================
# SEMANA 4 — TAREA
#
# TAREA 1  → Completa la zona de personalización
# TAREA 2  → Corre migraciones y crea superusuario
# TAREA 3 → Registra los modelos en admin.py
# TAREA 4 → Agrega 5 recursos reales desde el admin
#
# ENTREGA: admin.py completado + captura de pantalla del admin
#          con tus recursos + /recursos/ mostrando los datos.
# CRITERIO: admin.py registra Recurso con list_display útil.
# ============================================================

from django.shortcuts import render
from .models import Recurso

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Física"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente
# ════════════════════════════════════════════════════════════


def inicio(request):
    return render(request, 'hub/inicio.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'frase_mision': frase_mision,
    })


def acerca(request):
    return render(request, 'hub/acerca.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'anos_experiencia': anos_experiencia,
        'frase_mision': frase_mision,
    })


def recursos_view(request):
    recursos = Recurso.objects.all()
    return render(request, 'hub/recursos.html', {
        'nombre_docente': nombre_docente,
        'recursos': recursos,
    })
