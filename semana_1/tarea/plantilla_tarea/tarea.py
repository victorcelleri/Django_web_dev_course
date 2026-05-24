# ============================================================
# SEMANA 1 — TAREA: Clase Docente
#
# TAREA 1  → Completa los atributos con tu información
# TAREA 2  → Agrega el método describir_materias()
# TAREA 3  → Crea una segunda instancia de Docente
#
# ENTREGA: Este archivo tarea.py funcionando + tarea.html completado.
# CRITERIO: python tarea.py debe imprimir tu presentación real.
# ============================================================


class Docente:
    """Representa a un docente del hub personal."""

    def __init__(self, nombre, materia, institucion, anos_experiencia):
        # ============================================================
        # TAREA 1 — Los atributos ya están; personaliza los valores
        # abajo cuando crees la instancia (al final del archivo).
        # ============================================================
        self.nombre = nombre
        self.materia = materia
        self.institucion = institucion
        self.anos_experiencia = anos_experiencia

    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        print(f"Enseño {self.materia} en {self.institucion}.")
        print(f"Tengo {self.anos_experiencia} años de experiencia.")

    # ============================================================
    # TAREA 2 — Agrega el método describir_materias()
    # El método debe recibir una lista de materias y mostrarlas.
    #
    # Prompt Cursor (Ctrl+K):
    #   "Agrega un método describir_materias(self, lista_materias)
    #    que reciba una lista de strings e imprima cada materia
    #    numerada. Ejemplo: '1. Álgebra — 8° grado'"
    # ============================================================

    # ESCRIBE EL MÉTODO AQUÍ ↓


    # ============================================================
    # BONUS — generar_html()
    # Devuelve el bloque <header> de tu perfil.html con tus datos.
    # Este método anticipa exactamente lo que Django hará en Semana 2.
    #
    # Prompt Cursor (Ctrl+K):
    #   "Agrega un método generar_html(self) que devuelva un string
    #    con el bloque <header> de perfil.html usando f-string,
    #    insertando nombre, materia e institucion del docente."
    # ============================================================


# ============================================================
# TAREA 3 — Crea DOS instancias con datos reales
#   - La primera con TU información como docente
#   - La segunda con los datos de un colega imaginario
# ============================================================

mi_docente = Docente(
    nombre="",           # Tu nombre completo
    materia="",          # Tu materia principal
    institucion="",      # Tu institución
    anos_experiencia=0,  # Tus años de experiencia
)

mi_docente.presentarse()


# ── Puente hacia Django (Semana 2) ──────────────────────────────────────
# AHORA (Python puro):                       PRÓXIMA SEMANA (Django):
# ────────────────────────────────────────    ────────────────────────────────────────────
# class Docente:                          →   class Docente(models.Model):
#     self.nombre = nombre                →       nombre = models.CharField(max_length=100)
#     self.materia = materia              →       materia = models.CharField(max_length=100)
#
# mi_docente = Docente("García", ...)     →   mi_docente = Docente.objects.get(id=1)
# mi_docente.presentarse()               →   return render(request, 'perfil.html',
#                                                    {'docente': mi_docente})
#
# Django guarda los datos en base de datos y los inyecta en el HTML:
#   <h1>{{ docente.nombre }}</h1>
#   {% for m in docente.materias.all %} … {% endfor %}
