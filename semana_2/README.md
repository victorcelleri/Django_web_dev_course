# Semana 2: Instalación de Django, Patrón MVT y Ruteo Básico

> Django es un kit de construcción web: rutas, seguridad y servidor de desarrollo ya vienen resueltos.
> Esta semana conectas cada URL del Hub con una función Python que responde al navegador.

## Objetivo de Aprendizaje

Al finalizar esta semana podrás **instalar Django, crear un proyecto y una aplicación**, definir rutas en `urls.py` y escribir vistas en `views.py` que devuelven páginas web.

---

## El concepto

Django organiza el trabajo con **MVT**: Modelo (datos, semana 4), Vista (lógica, esta semana) y Plantilla (presentación, semana 3). El **ruteo** es el índice que une cada URL (`/acerca/`) con la función correcta en `views.py`.

**Analogía MVT:** el modelo es el libro de calificaciones, la vista es el docente que decide qué mostrar, la plantilla es la boleta que recibe el estudiante.

## En el Hub Personal del Docente

Defines las rutas del sitio (`/`, `/acerca/`, etc.) y vistas que por ahora devuelven HTML con `HttpResponse`. Es el esqueleto navegable del Hub antes de separar plantillas y base de datos.

---

## Actividades de la semana

| Actividad | Carpeta | Tema | Descripción |
|-----------|---------|------|-------------|
| **Demo** | `demo/inicio/` → `demo/finalizado/` | Primer servidor Django y rutas | Partes de `hub/urls.py` ya conectado y `views.py` vacío. En vivo instalas/ejecutas Django, escribes `inicio()` y `acerca()` con `HttpResponse` y registras las rutas. El finalizado muestra el Hub navegable en `http://127.0.0.1:8000/`. |
| **Actividad en clase** | `ejercicio_clase/plantilla/` | Vista `acerca()` | Personalizas la zona de datos del docente. La vista `inicio()` ya está dada; creas `acerca()` con HTML propio y actualizas `hub/urls.py`. Criterio: `/acerca/` muestra tu información real. |
| **Tarea** | `tarea/plantilla_tarea/` | Tercera ruta libre | Completas variables, pruebas `inicio()` y `acerca()` ya construidas, y diseñas una tercera vista y URL a tu elección (horario, materias, contacto, etc.) con `HttpResponse`. Criterio: las 3 rutas funcionan en el navegador. |

---

## Patrón MVT de Django

| Capa | Archivo | Responsabilidad |
|------|---------|----------------|
| **M**odelo | `hub/models.py` | Estructura de datos (semana 4) |
| **V**ista | `hub/views.py` | Lógica: qué responder a cada solicitud |
| **T**emplate | `templates/` | HTML separado (semana 3) |

Esta semana nos enfocamos en la **Vista** y el **ruteo**.

| Componente | Analogía docente |
|------------|------------------|
| `urls.py` | Mapa del colegio: qué hay en cada sala |
| `views.py` | Cada docente con su escritorio (función por página) |
| `settings.py` | Reglamento interno del proyecto |
| `manage.py` | Herramienta para servidor, migraciones y apps |

---

## Fuente de Verdad de Cada Archivo

| Archivo | Responsabilidad |
|---------|----------------|
| `manage.py` | Herramienta de línea de comandos de Django. No modificar. |
| `hub_docente/settings.py` | Configuración global (apps instaladas, base de datos, etc.) |
| `hub_docente/urls.py` | Punto de entrada de todas las URLs del proyecto |
| `hub/urls.py` | URLs específicas de la app `hub` |
| `hub/views.py` | **Archivo principal esta semana**: funciones que responden a cada URL |

---

## Sintaxis esencial

| Sintaxis | Qué hace | Ejemplo |
|----------|----------|---------|
| `def vista(request):` | Define una vista | `def inicio(request):` |
| `return HttpResponse("...")` | Responde HTML/texto | `return HttpResponse("<h1>Hola</h1>")` |
| `path("ruta/", vista, name="...")` | Registra una URL | `path("acerca/", views.acerca, name="acerca")` |
| `include("hub.urls")` | Incluye rutas de la app | En `hub_docente/urls.py` |

---

## Comandos Clave

```bash
pip install django
python manage.py runserver
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/acerca/
```

---

## Cómo Funciona el Ruteo

```
Navegador pide: http://127.0.0.1:8000/acerca/
         ↓
hub_docente/urls.py → include de hub.urls
         ↓
hub/urls.py → 'acerca/' → views.acerca
         ↓
hub/views.py → acerca(request) devuelve HttpResponse
         ↓
Navegador muestra la página
```

---

## Errores comunes

1. **App sin registrar en `INSTALLED_APPS`** — agrega `"hub"` en `settings.py`.
2. **Import con nombre incorrecto** — el nombre debe coincidir con la carpeta de la app.
3. **Ruta sin barra final** — usa `"acerca/"`, no `"acerca"`.
4. **`runserver` fuera de la carpeta de `manage.py`** — ejecuta el comando donde está `manage.py`.

---

## Glosario

- **Framework:** herramientas prefabricadas para un tipo de software (Django = web).
- **Vista:** función que recibe `request` y devuelve una respuesta (no es “pantalla”).
- **Ruteo:** asociar URL → vista según `urls.py`.
- **`HttpResponse`:** empaqueta lo que el navegador muestra.

---

## Siguiente semana

Escribir HTML dentro de strings Python es incómodo. La semana 3 usa plantillas Django y `render()` para separar presentación y lógica.

---

## Prompts de Cursor AI para Esta Semana

**Prompt 1 — Crear una vista básica:**
> "En este archivo views.py de Django, crea una función llamada `inicio` que reciba `request` y devuelva un `HttpResponse` con HTML que muestre mi nombre '[tu nombre]', mi materia '[tu materia]' y un enlace a `/acerca/`."

**Prompt 2 — Agregar una ruta en urls.py:**
> "En este hub/urls.py de Django, agrega una ruta para la URL `/horario/` que llame a una función `horario` en views.py."

**Prompt 3 — Entender el patrón MVT:**
> "Explica el patrón MVT de Django (Modelo-Vista-Template) con un ejemplo simple para un docente que nunca programó. ¿Cómo se diferencia de escribir HTML directo?"

**Prompt 4 — Pasar datos a la vista:**
> "En esta vista de Django que usa HttpResponse, agrega una lista de 3 materias como variable Python y muéstralas como elementos `<li>` dentro de un `<ul>` en el HTML devuelto."
