# ============================================================
# SEMANA 1 — INICIO: De variables sueltas a una clase
# Ejecutar: python docente.py
# ============================================================


# ════════════════════════════════════════════════════════════
# PROBLEMA: datos sueltos, sin estructura
# ════════════════════════════════════════════════════════════
nombre      = "Prof. García"
materia     = "Matemáticas"
institucion = "Colegio Simón Bolívar"
experiencia = 10

# ¿Y si necesitamos un segundo docente? → duplicamos todo. ❌


# ════════════════════════════════════════════════════════════
# SOLUCIÓN: una clase agrupa datos + comportamiento
# ════════════════════════════════════════════════════════════

class Docente:
    """Representa a un docente con su información pública."""

    # TODO EN VIVO — el profesor escribe el cuerpo de __init__:
    def __init__(self, nombre, materia, institucion, anos_experiencia):
        pass

    # TODO EN VIVO — el profesor escribe el cuerpo de presentarse:
    def presentarse(self):
        pass

# ── Uso (descomentar al terminar __init__ y presentarse) ────
# docente_1 = Docente("Prof. García", "Matemáticas", "C. Simón Bolívar", 10)
# docente_2 = Docente("Prof. Rodríguez", "Historia", "Liceo Central", 5)
# docente_1.presentarse()
# docente_2.presentarse()
