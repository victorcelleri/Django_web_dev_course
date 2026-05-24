# Desarrollo Web con Python y Django — Hub Personal del Docente

Curso de 5 semanas para docentes. Cada semana construyes una pieza del **Hub Personal del Docente**: un sitio web real donde compartes recursos con tus estudiantes, recibes mensajes y administras todo desde el Panel de Administración de Django.

---

## ¿Qué Vas a Construir?

Una aplicación web con Django que incluye:
- Página de inicio donde te presentas y describes tus cursos
- Página de recursos con enlaces y materiales para estudiantes
- Formulario de contacto para recibir mensajes
- Panel de administración para gestionar todo el contenido

---

## Herramientas del Curso

| Herramienta | Uso en el curso |
|-------------|----------------|
| **Python 3.10+** | Lenguaje base |
| **Django 4.2** | Framework web completo con patrón MVT |
| **SQLite** | Base de datos integrada en Django |
| **Bootstrap 5** | Diseño profesional sin escribir CSS desde cero |
| **Cursor AI** | Editor con IA para escribir y entender código |

---

## Estructura del Curso por Semana

| Semana | Tema | Habilidad principal |
|--------|------|---------------------|
| Semana 1 | HTML y Python | Entender la web y las bases del lenguaje |
| Semana 2 | Django y Rutas | Instalar Django y crear tu primer servidor |
| Semana 3 | Plantillas Dinámicas | Separar HTML de Python con el motor de plantillas |
| Semana 4 | Modelos y Admin | Guardar datos y administrarlos visualmente |
| Semana 5 | Formularios y Despliegue | Recibir mensajes y publicar el sitio en internet |

---

## Anatomía de Cada Semana

```
semana_X/
├── README.md                  ← Objetivos, conceptos y prompts para Cursor
├── demo/
│   ├── inicio/                ← Código al INICIO de la clase (el profesor parte de aquí)
│   └── finalizado/            ← Código TERMINADO después de la demo en vivo
├── ejercicio_clase/
│   └── plantilla/             ← Plantilla con guías [Ctrl+K] para el ejercicio en clase
└── tarea/
    └── plantilla_tarea/       ← Punto de partida para el trabajo en casa
```

---

## Actividades por semana

Cada semana sigue el mismo esquema: **Demo** (profesor en vivo, `demo/inicio` → `demo/finalizado`), **Actividad en clase** (`ejercicio_clase/plantilla/`) y **Tarea** (`tarea/plantilla_tarea/`). Detalle completo en el `README.md` de cada semana.

| Semana | Actividad | Tema | Descripción |
|--------|-----------|------|-------------|
| **1** | Demo | HTML y clase `Docente` | Construcción en vivo de `perfil.html` y `docente.py` desde HTML vacío. |
| **1** | Actividad en clase | `presentarse()` | Completar `ejercicio.html` y método `presentarse()` en la clase `Docente`. |
| **1** | Tarea | Docente ampliado | Método `describir_materias()`, segunda instancia y entrega `tarea.py` + `tarea.html`. |
| **2** | Demo | Django y rutas | Vistas `inicio()` y `acerca()` con `HttpResponse` y servidor local. |
| **2** | Actividad en clase | Vista `acerca()` | Crear la página Acerca con ruta propia (inicio ya dado). |
| **2** | Tarea | Tercera ruta | Añadir una vista y URL adicional a elección del docente. |
| **3** | Demo | Plantillas y `render()` | `base.html` con Bootstrap, herencia y refactor desde `HttpResponse`. |
| **3** | Actividad en clase | Plantillas dinámicas | Convertir `acerca()` y crear `recursos_view()` con contexto. |
| **3** | Tarea | Recursos propios | Lista de recursos reales y página `/recursos/` completa. |
| **4** | Demo | Modelos y admin | `Recurso`, `Mensaje`, migraciones y Panel de Administración. |
| **4** | Actividad en clase | Modelo `Recurso` | Definir modelo, migrar y cargar 3 recursos desde `/admin/`. |
| **4** | Tarea | Modelo `Mensaje` | Definir `Mensaje`, registrar en admin y cargar 5 recursos. |
| **5** | Demo | POST, CSRF y `.env` | Formulario de contacto, validación y configuración de producción. |
| **5** | Actividad en clase | Vista `contacto()` | Completar guardado de mensajes con `ContactoForm`. |
| **5** | Tarea | PythonAnywhere | Publicar el Hub con URL pública en internet. |

---

## Instalación Rápida

```bash
# 1. Instalar Python 3.10+ desde python.org
# 2. Instalar dependencias del curso
pip install -r requirements.txt
# 3. Para semanas 2-5, navegar a la carpeta del proyecto y ejecutar:
python manage.py runserver
# 4. Abrir el navegador en: http://127.0.0.1:8000
```

