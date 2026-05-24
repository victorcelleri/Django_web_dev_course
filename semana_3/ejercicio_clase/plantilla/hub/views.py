# ============================================================
# SEMANA 3 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa la zona de personalización
# EJERCICIO 2 → Convierte acerca() a render()
# EJERCICIO 3  → Crea recursos_view() con render()
#
# ENTREGA: Este archivo views.py con las 3 vistas completadas.
# CRITERIO: Las 3 URLs renderizan plantillas (sin HttpResponse).
# ============================================================

from django.shortcuts import render

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Ciencias Naturales"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente

recursos_lista = [
    # {"titulo": "Nombre del sitio", "url": "https://...", "descripcion": "Para qué sirve"},
]
# ════════════════════════════════════════════════════════════


def inicio(request):
    return render(request, 'hub/inicio.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'frase_mision': frase_mision,
    })


# ============================================================
# EJERCICIO — Convierte acerca() a render()
#
# Prompt Cursor (Ctrl+K):
#   "Convierte esta vista a render(). Crea el contexto con
#    nombre_docente, materia, institucion y anos_experiencia.
#    La plantilla a usar es 'hub/acerca.html'."
# ============================================================
def acerca(request):
    # COMPLETA EL CONTEXTO Y USA render() ↓
    pass


# ============================================================
# EJERCICIO — Crea recursos_view() con render()
#
# Prompt Cursor (Ctrl+K):
#   "Crea la vista recursos_view que use render() con la
#    plantilla 'hub/recursos.html' y pase la lista
#    recursos_lista en el contexto bajo la clave 'recursos'."
# ============================================================
# ESCRIBE AQUÍ ↓
