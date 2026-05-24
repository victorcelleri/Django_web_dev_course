# ============================================================
# SEMANA 2 — TAREA
#
# TAREA 1  → Completa las variables con tu información
# TAREA 2  → Lee y ejecuta las vistas ya construidas
# TAREA 3 → Crea una tercera vista de tu elección
#
# ENTREGA: Este archivo views.py + hub/urls.py actualizados.
# CRITERIO: Las 3 rutas deben funcionar en el navegador.
# ============================================================

from django.http import HttpResponse

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Matemáticas"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente
# ════════════════════════════════════════════════════════════


def inicio(request):
    return HttpResponse(f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>{nombre_docente}</title>
<style>
    body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }}
    nav {{ background: #2D4A7A; padding: 12px 20px; border-radius: 6px; margin-bottom: 24px; }}
    nav a {{ color: white; text-decoration: none; margin-right: 16px; }}
</style></head>
<body>
    <nav><a href="/">Inicio</a> <a href="/acerca/">Acerca</a></nav>
    <h1>{nombre_docente}</h1>
    <p>Docente de {materia} &middot; {institucion}</p>
</body></html>""")


def acerca(request):
    return HttpResponse(f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>Acerca</title>
<style>
    body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }}
    nav {{ background: #2D4A7A; padding: 12px 20px; border-radius: 6px; margin-bottom: 24px; }}
    nav a {{ color: white; text-decoration: none; margin-right: 16px; }}
</style></head>
<body>
    <nav><a href="/">Inicio</a> <a href="/acerca/">Acerca</a></nav>
    <h1>Acerca de {nombre_docente}</h1>
    <p>{materia} &middot; {institucion} &middot; {anos_experiencia} años de experiencia</p>
    <p><a href="/">&larr; Volver</a></p>
</body></html>""")


# ============================================================
# TAREA 3 — Crea UNA vista adicional a tu elección
#
# Opciones:
#   /horario/   → Tu horario semanal de clases
#   /recursos/  → 3 sitios web útiles para tus estudiantes
#   /materias/  → Las materias que enseñas este semestre
#
# Pasos:
# 1. Escribe la función aquí abajo
# 2. Agrega la ruta en hub/urls.py
#
# Prompt Cursor (Ctrl+K):
#   "Crea una vista Django llamada [nombre] que devuelva
#    un HttpResponse con HTML mostrando [contenido].
#    Usa el mismo estilo CSS de las vistas de arriba
#    e incluye el nav con los enlaces existentes."
# ============================================================

# ESCRIBE TU VISTA AQUÍ ↓
