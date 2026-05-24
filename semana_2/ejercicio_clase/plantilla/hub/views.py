# ============================================================
# SEMANA 2 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa la zona de personalización
# EJERCICIO 2 → Crea la vista acerca()
#
# ENTREGA: Este archivo views.py + hub/urls.py actualizados.
# CRITERIO: /acerca/ muestra tu información real.
# ============================================================

from django.http import HttpResponse

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Lengua y Literatura"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente
# ════════════════════════════════════════════════════════════


def inicio(request):
    return HttpResponse(f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{nombre_docente}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }}
        nav {{ background: #2D4A7A; padding: 12px 20px; border-radius: 6px; margin-bottom: 24px; }}
        nav a {{ color: white; text-decoration: none; margin-right: 16px; }}
        h1 {{ color: #2D4A7A; }}
    </style>
</head>
<body>
    <nav>
        <a href="/">Inicio</a>
        <a href="/acerca/">Acerca</a>
    </nav>
    <h1>Bienvenidos al aula de {nombre_docente}</h1>
    <p>Docente de {materia} &middot; {institucion}</p>
    <p><a href="/acerca/">Conóceme &rarr;</a></p>
</body>
</html>""")


# ============================================================
# EJERCICIO — Crea la vista acerca()
#
# Coloca el cursor aquí abajo y presiona Ctrl+K en Cursor.
# Escribe este prompt:
#
#   "Crea una vista Django llamada acerca que devuelva un
#    HttpResponse con HTML. Debe mostrar el nombre_docente,
#    materia, institucion y anos_experiencia en tarjetas.
#    Incluye un enlace de vuelta a /. Usa el mismo estilo
#    CSS inline que tiene la función inicio() arriba."
# ============================================================

# ESCRIBE TU CÓDIGO AQUÍ ↓
