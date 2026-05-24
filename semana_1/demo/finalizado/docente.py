# ============================================================
# SEMANA 1 — FINALIZADO: Clase Docente completa
# Ejecutar: python docente.py
# ============================================================


class Docente:
    """Representa a un docente con su información pública."""

    # __init__ se ejecuta automáticamente al crear un objeto.
    # 'self' es la referencia al objeto que se está creando.
    def __init__(self, nombre, materia, institucion, anos_experiencia):
        self.nombre           = nombre            # atributo de instancia
        self.materia          = materia
        self.institucion      = institucion
        self.anos_experiencia = anos_experiencia

    # Un método es una función que "pertenece" al objeto.
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        print(f"Enseño {self.materia} en {self.institucion}.")
        print(f"Tengo {self.anos_experiencia} años de experiencia.")

    # Bonus: genera el bloque <header> de perfil.html con los datos del docente.
    def generar_html(self):
        return (
            f"<header>\n"
            f"    <h1>{self.nombre}</h1>\n"
            f"    <p>Docente de {self.materia} · {self.institucion}</p>\n"
            f"</header>"
        )


# ── Uso: un objeto por docente, sin duplicar código ─────────
docente_1 = Docente("Prof. García",    "Matemáticas", "Colegio Dolores Sucre", 10)
docente_2 = Docente("Prof. Rodríguez", "Historia",   "Colegio Dolores Sucre", 5)

docente_1.presentarse()
print()
docente_2.presentarse()

# ── Puente hacia Django (Semana 2) ───────────────────────────
# AHORA (Python puro)               → PRÓXIMA SEMANA (Django)
# ─────────────────────────────────────────────────────────────
# class Docente:                    → class Docente(models.Model):
#     self.nombre = nombre          →     nombre = models.CharField(max_length=100)
#     self.materia = materia        →     materia = models.CharField(max_length=100)
#
# Django también guarda los datos en base de datos y los inyecta
# en el HTML automáticamente: <h1>{{ docente.nombre }}</h1>
