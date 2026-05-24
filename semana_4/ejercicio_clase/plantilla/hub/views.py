# ============================================================
# SEMANA 4 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa la zona de personalización
# EJERCICIO 2 → Corre las migraciones y abre /admin/
# EJERCICIO 3 → Agrega 3 recursos reales desde el admin
#
# ENTREGA: Captura de pantalla del admin con tus recursos cargados
#          + /recursos/ mostrando esos recursos en el navegador.
# CRITERIO: Los datos reales aparecen en la página /recursos/.
# ============================================================

from django.shortcuts import render
from .models import Recurso

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Biología"
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


# ── EJERCICIO 2 y 3: Esta vista ya consulta la base de datos ──
# Pasos:
#   1. Abre una terminal en VS Code y ejecuta:
#        python manage.py makemigrations
#        python manage.py migrate
#        python manage.py createsuperuser
#   2. Corre el servidor: python manage.py runserver
#   3. Ve a http://127.0.0.1:8000/admin/ e inicia sesión
#   4. En "Recursos" agrega 3 recursos reales para tu materia
#   5. Ve a /recursos/ y verifica que aparecen en la página
#
# Prompt Cursor (Ctrl+K si quieres explorar):
#   "¿Qué hace Recurso.objects.all() en Django ORM?"
def recursos_view(request):
    recursos = Recurso.objects.all()
    return render(request, 'hub/recursos.html', {
        'nombre_docente': nombre_docente,
        'recursos': recursos,
    })
