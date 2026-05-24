# ============================================================
# SEMANA 3 — TAREA
#
# TAREA 1  → Completa las variables con tu información
# TAREA 2  → Lee las vistas inicio() y acerca() ya dadas
# TAREA 3 → Crea tu propia lista de recursos y
#                    completa recursos_view() con render()
#
# ENTREGA: views.py + templates/hub/recursos.html completados.
# CRITERIO: Las 3 URLs muestran tu contenido real.
# ============================================================

from django.shortcuts import render

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Historia"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente

recursos_lista = [
    # {"titulo": "Nombre del sitio", "url": "https://...", "descripcion": "Para qué sirve"},
    # Agrega al menos 3 recursos reales de tu materia
]
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
    })


# ── TAREA 3: Completa esta vista ────────────────────────────
def recursos_view(request):
    # Prompt Cursor (Ctrl+K):
    #   "Completa esta vista para que use render() con la
    #    plantilla 'hub/recursos.html' y pase recursos_lista
    #    bajo la clave 'recursos' y nombre_docente en el contexto."
    pass
