# Semana 1: Fundamentos de la Web (HTML) y Python

> Hoy construyes una página web con HTML puro y aprendes las bases de Python
> que Django usará automáticamente en las semanas siguientes.
> Al terminar, entenderás qué es una etiqueta, una función y un objeto.

## Objetivo de Aprendizaje

Al finalizar esta semana podrás **escribir una página HTML básica** y **crear funciones y clases en Python** — las dos piezas que Django combina para construir sitios web.

---

## El concepto

HTML define la **estructura** de una página (títulos, párrafos, enlaces); no programa, solo organiza lo que ve el navegador. Python sí es un lenguaje de programación: variables, funciones y clases serán la lógica que en semanas siguientes alimentará las vistas y modelos de Django.

**Analogía:** HTML es la planilla en papel; Python es la lógica que decide qué escribir en cada celda. Juntos preparan un Hub que dejará de ser estático.

## En el Hub Personal del Docente

El HTML de esta semana es la base visual de inicio, recursos y contacto. La clase `Docente` en Python anticipa los modelos y vistas: nombre, materia e institución que más adelante vendrán de la base de datos.

---

## Actividades de la semana


| Actividad              | Carpeta                             | Tema                                     | Descripción                                                                                                                                                                                                                                                                                                                                                                  | Entrega                          |
| ---------------------- | ----------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **Demo**               | `demo/inicio/` → `demo/finalizado/` | Página HTML y clase `Docente`            | El profesor parte de `demo/inicio/perfil.html` — la página ya tiene toda la estructura HTML y CSS — y recorre en vivo las secciones (nav, hero, estadísticas, materias, recursos, contacto), las variables CSS del `:root` y los conceptos de flexbox. Luego muestra `docente.py`: la clase `Docente` con sus atributos y métodos. El estado final (`demo/finalizado/`) añade comentarios didácticos en el CSS y las marcas `{{ docente.nombre }}` que anticipan Django. | N/A                              |
| **Actividad en clase** | `ejercicio_clase/plantilla/`        | Personalización HTML y método `presentarse()` | En `ejercicio.html`: cambias el título (EJ1, 2 min), completas el header con tu nombre y materia (EJ2, 3 min), escribes la sección "Acerca de mí" usando Cursor Ctrl+K (EJ3, 5 min) y agregas tu lista de materias (EJ4, 5 min). En `ejercicio.py`: completas las cuatro variables con tu información (EJ1, 5 min) y agregas el método `presentarse()` con Cursor Ctrl+K (EJ2, 15 min). | `ejercicio.py` + `ejercicio.html` |
| **Tarea**              | `tarea/plantilla_tarea/`            | Clase `Docente` ampliada                 | Personalizas la instancia del docente con tus datos reales, implementas `describir_materias()` con una lista de tus materias actuales y creas una segunda instancia de `Docente`. En `tarea.html` completas la página con tu información. `python tarea.py` debe imprimir tu presentación real.                                                                              | `tarea.py` + `tarea.html`        |


---

## Fuente de Verdad de Cada Archivo


| Actividad              | Archivo          | Responsabilidad                                                                     |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------------- |
| Demo                   | `perfil.html`    | Página HTML completa del docente: secciones, variables CSS y estilos flexbox        |
| Demo                   | `docente.py`     | Clase Python `Docente` con atributos (`nombre`, `materia`, `institucion`, `anos_experiencia`) y métodos |
| Ejercicio en clase     | `ejercicio.html` | HTML del ejercicio en clase: header, sección "Acerca de mí" y lista de materias    |
| Ejercicio en clase     | `ejercicio.py`   | Python del ejercicio: variables de personalización y método `presentarse()`         |
| Tarea                  | `tarea.html`     | HTML de la tarea: página personalizada completa con la información del docente      |
| Tarea                  | `tarea.py`       | Python de la tarea: clase con `presentarse()`, `describir_materias()` y segunda instancia |


> **Por qué importa:** Django usa Python para la lógica (vistas = funciones) y HTML para la presentación (plantillas). Esta semana separa y practica cada parte antes de combinarlas.

---

## Teoría


| Concepto        | Qué hace                           | Analogía docente                          |
| --------------- | ---------------------------------- | ----------------------------------------- |
| Etiqueta HTML   | Define un elemento visual          | Formato de sección en un informe          |
| Variable Python | Guarda un dato                     | Nombre en una casilla de formulario       |
| Función Python  | Agrupa instrucciones reutilizables | Rutina que repites cada semana            |
| Clase / objeto  | Agrupa datos y acciones            | Ficha del estudiante con nombre y métodos |
| Atributo HTML   | Información extra en una etiqueta  | Columnas extra de una planilla            |


### HTML


| Etiqueta                     | Qué hace                        |
| ---------------------------- | ------------------------------- |
| `<!DOCTYPE html>`            | Declara que el archivo es HTML5 |
| `<html>`, `<head>`, `<body>` | Estructura base del documento   |
| `<h1>` … `<h6>`              | Títulos de mayor a menor tamaño |
| `<p>`                        | Párrafo de texto                |
| `<a href="url">`             | Enlace a otra página            |
| `<ul>` / `<li>`              | Lista desordenada               |
| `<strong>` / `<em>`          | Texto en negrita / cursiva      |


### Python


| Sintaxis           | Qué hace              | Ejemplo                        |
| ------------------ | --------------------- | ------------------------------ |
| `nombre = "valor"` | Variable              | `nombre_docente = "Andrea"`    |
| `def nombre():`    | Función               | `def saludar():`               |
| `class Nombre:`    | Clase                 | `class Docente:`               |
| `self.atributo`    | Atributo de instancia | `self.materia = "Matemáticas"` |
| f-string           | Texto con variables   | `f"Soy {self.nombre}"`         |


---

## Conexión con Django (preview)

```
HTML de esta semana  →  Plantillas Django (semana 3)
Funciones Python     →  Vistas Django en views.py (semana 2)
Clases Python        →  Modelos Django en models.py (semana 4)
```

---

## Errores comunes

1. **Etiquetas HTML sin cerrar** — cada `<p>` necesita `</p>`. Revisa la vista previa del navegador.
2. **Indentación en Python** — usa 4 espacios por nivel; no mezcles tabuladores y espacios.
3. **Olvidar `self` en métodos** — `def mi_metodo(self):` es obligatorio en clases.
4. **Comillas sin cerrar** — abre y cierra con el mismo tipo (`"` o `'`).

---

## Glosario

- **HTML:** lenguaje de estructura de páginas web.
- **Etiqueta:** par `<p>` … `</p>` que envuelve un elemento.
- **Variable / función / clase / objeto / método / atributo:** bloques básicos de Python usados en todo el curso.

---

## Siguiente semana

Las páginas HTML son estáticas: para cambiar un dato hay que editar el archivo. La semana 2 instala Django y conecta URLs con funciones Python para responder con contenido dinámico.

---

## Cómo Ejecutar

```bash
# Abrir el HTML en el navegador:
# Doble clic en el archivo .html, o arrastrarlo al navegador

# Ejecutar el script Python:
python docente.py
```

---

## Prompts de Cursor AI para Esta Semana

**Prompt 1 — Crear la estructura HTML:**

> "Crea un archivo HTML5 completo para un docente llamado [tu nombre] que enseña [tu materia]. Incluye: título en el `<head>`, un `<h1>` con el nombre, un `<p>` con la institución, una lista `<ul>` con 3 materias, y un enlace de correo con `<a href='mailto:'>`. Usa estilos inline básicos en el `<body>` para un fondo claro y fuente sans-serif."

**Prompt 2 — Agregar una sección al HTML:**

> "En este archivo HTML, agrega una sección `<section>` después de la lista de materias. La sección debe tener un `<h2>` que diga 'Mis Recursos' y tres `<a href>` con enlaces a sitios educativos útiles para mis estudiantes."

**Prompt 3 — Crear la clase Docente:**

> "Crea una clase Python llamada `Docente` con los atributos: nombre, materia, institucion y anos_experiencia. Agrega un método `presentarse()` que imprima una presentación completa, y un método `generar_html()` que devuelva un string con HTML básico usando los atributos del docente."

**Prompt 4 — Entender la conexión con Django:**

> "Explica, para un docente que nunca programó, cómo el HTML que escribí esta semana se convierte en plantillas de Django, y cómo la clase Python que escribí se convierte en un Modelo de Django."

