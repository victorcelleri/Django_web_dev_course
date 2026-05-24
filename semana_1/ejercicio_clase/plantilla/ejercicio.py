# ============================================================
# SEMANA 1 — EJERCICIO EN CLASE
#
# EJERCICIO 1  → Completa las variables con tu información
# EJERCICIO 2 → Agrega el método presentarse() a la clase
# ============================================================


# ── EJERCICIO 1: Completa las variables ─────────────────────
nombre = ""          # Tu nombre. Ej: "Prof. Ramírez"
materia = ""         # Tu materia. Ej: "Ciencias Naturales"
institucion = ""     # Tu institución
anos = 0             # Años de experiencia


# ── La clase ya tiene __init__ — solo falta presentarse() ───
class Docente:

    def __init__(self, nombre, materia, institucion, anos_experiencia):
        self.nombre = nombre
        self.materia = materia
        self.institucion = institucion
        self.anos_experiencia = anos_experiencia

    # ============================================================
    # EJERCICIO 2 — Agrega el método presentarse()
    #
    # El método debe imprimir:
    #   "Hola, soy [nombre]."
    #   "Enseño [materia] en [institucion]."
    #   "Tengo [años] años de experiencia."
    #
    # Prompt Cursor (Ctrl+K):
    #   "Agrega un método presentarse(self) a esta clase
    #    que imprima tres líneas con los atributos del docente."
    # ============================================================

    # ESCRIBE EL MÉTODO AQUÍ ↓


# Prueba tu clase con tus datos reales
mi_docente = Docente(
    nombre=nombre,
    materia=materia,
    institucion=institucion,
    anos_experiencia=anos,
)

mi_docente.presentarse()


# ── Puente hacia Django (Semana 2) ──────────────────────────────────────
# AHORA (Python puro):                    PRÓXIMA SEMANA (Django):
# ─────────────────────────────────────────────────────────────────────────
# mi_docente = Docente("García", ...)  →  Docente.objects.get(id=1)
# mi_docente.presentarse()             →  return render(request, 'perfil.html',
#                                                 {'docente': mi_docente})
#
# Django usará los mismos atributos (nombre, materia, institucion…)
# para inyectarlos en el HTML: <h1>{{ docente.nombre }}</h1>
