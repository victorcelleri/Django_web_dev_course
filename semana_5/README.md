# Semana 5: Formularios Interactivos (POST) y Despliegue en PythonAnywhere

> GET pide la página; POST envía el formulario de contacto.
> El token CSRF es el sello que Django exige antes de guardar un mensaje en la base de datos.

## Objetivo de Aprendizaje

Al finalizar esta semana podrás **recibir y guardar mensajes de contacto** con un formulario Django, y **publicar tu Hub Personal del Docente en internet** usando PythonAnywhere de forma gratuita.

---

## El concepto

**POST** empaqueta los datos del formulario en el cuerpo de la solicitud (no en la URL). Django valida con `ContactoForm` en `hub/forms.py`; la vista `contacto()` distingue GET (mostrar) y POST (guardar un `Mensaje`).

**CSRF:** `{% csrf_token %}` dentro de `<form method="post">` evita envíos falsos desde otros sitios. Sin él, error **403**.

**Despliegue:** en producción, `DEBUG=False`, `ALLOWED_HOSTS` con tu dominio, variables en `.env` y `collectstatic` para CSS.

## En el Hub Personal del Docente

Completas `/contacto/`: el visitante envía nombre, correo y mensaje; Django los guarda y muestra confirmación. Luego subes el proyecto a PythonAnywhere con URL pública.

---

## Actividades de la semana

| Actividad | Carpeta | Tema | Descripción |
|-----------|---------|------|-------------|
| **Demo** | `demo/inicio/` → `demo/finalizado/` | Formulario POST, CSRF y producción | Partes de la semana 4 sin formulario de contacto. En vivo creas `ContactoForm`, la vista `contacto()` (GET/POST), plantilla con `{% csrf_token %}`, `.env` y ajustes de `settings.py`. El finalizado incluye mensajes guardados en BD y configuración lista para desplegar. |
| **Actividad en clase** | `ejercicio_clase/plantilla/` | Vista `contacto()` | `forms.py` y plantilla ya están dados. Personalizas datos del docente y completas `contacto()` para validar el formulario, guardar `Mensaje` y mostrar confirmación con `messages`. Criterio: el formulario persiste mensajes en la BD. |
| **Tarea** | `tarea/plantilla_tarea/` | Despliegue en PythonAnywhere | Personalizas el Hub, pruebas el formulario en local, adaptas mensaje de éxito y sigues la guía del README para publicar en PythonAnywhere (migrate, variables de entorno, `collectstatic`, WSGI). Entrega: URL pública del Hub en funcionamiento. |

---

## Fuente de Verdad de Cada Archivo

| Archivo | Responsabilidad |
|---------|----------------|
| `hub/forms.py` | `ContactoForm` con validación automática |
| `hub/views.py` | `contacto()` maneja GET y POST |
| `templates/hub/contacto.html` | Formulario, CSRF y mensajes Django |
| `.env.ejemplo` | Plantilla de variables; copiar a `.env` |
| `hub_docente/settings.py` | Lee `SECRET_KEY` y `DEBUG` desde `.env` |
| `requirements.txt` | Dependencias con versiones fijas |

> **Regla de producción:** nunca pongas `SECRET_KEY` ni contraseñas en el código. Usa variables de entorno.

---

## Teoría

| Concepto | Qué hace | Analogía docente |
|----------|----------|------------------|
| GET | Solicita página sin enviar datos | Abrir el catálogo |
| POST | Envía datos del formulario | Entregar solicitud firmada |
| Token CSRF | Valida origen del envío | Sello en documento oficial |
| `request.method` | `'GET'` o `'POST'` | ¿Trajo el formulario lleno? |
| `form.is_valid()` | Valida campos del formulario Django | Revisar que no falte nada |
| `DEBUG = False` | Modo producción | No mostrar errores técnicos al público |
| `ALLOWED_HOSTS` | Dominios permitidos | Aulas autorizadas |
| `wsgi.py` | Entrada del servidor web | Puerta principal del colegio |

---

## Ciclo de Vida del Formulario

```
1. Usuario visita /contacto/  → GET → formulario vacío (ContactoForm)
2. Usuario envía            → POST → form.is_valid()
3. Si hay errores           → re-muestra formulario con mensajes
4. Si es válido             → Mensaje.objects.create(...) + messages.success + redirect
```

---

## Token CSRF — obligatorio

```html
<form method="post">
    {% csrf_token %}
    ...
</form>
```

---

## Vista de referencia (simplificada)

```python
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(request, '¡Mensaje recibido!')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'hub/contacto.html', {'form': form, ...})
```

---

## Comandos Clave

```bash
pip install -r requirements.txt
copy .env.ejemplo .env   # Windows; en Linux: cp .env.ejemplo .env
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic   # antes de producción
python manage.py runserver
```

### Producción en `settings.py`

```python
DEBUG = False
ALLOWED_HOSTS = ["tuusuario.pythonanywhere.com"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

## Guía de Despliegue en PythonAnywhere

1. Cuenta gratuita en [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Files** → subir el proyecto
3. **Bash:** `pip3.10 install --user -r requirements.txt`
4. **Bash:** `python manage.py migrate` y `collectstatic`
5. **Web** → Add web app → Manual config → Python 3.10
6. WSGI → apuntar a `hub_docente/wsgi.py`
7. Variables de entorno (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
8. **Static files** → carpeta `staticfiles`
9. **Reload** → visitar `tuusuario.pythonanywhere.com`

---

## Errores comunes

1. **403 CSRF** — falta `{% csrf_token %}` en la plantilla.
2. **Reenvío al recargar** — usa `redirect()` tras guardar (POST-Redirect-GET).
3. **DisallowedHost** — agrega tu dominio en `ALLOWED_HOSTS`.
4. **CSS sin cargar** — `DEBUG=False` requiere `collectstatic` y configurar estáticos en PythonAnywhere.

---

## Glosario

- **POST / GET:** métodos HTTP para enviar o solicitar páginas.
- **CSRF:** ataque de formulario falso; el token lo previene.
- **Deployment:** publicar la app en un servidor accesible desde internet.
- **WSGI:** interfaz entre el servidor web y Django (PythonAnywhere la configura).

---

## Cierre del curso

Con el despliegue, el Hub queda en línea: inicio, acerca, recursos, contacto y `/admin/`. Pasos naturales después: autenticación de usuarios, subida de archivos PDF y CSS personalizado.

---

## Prompts de Cursor AI para Esta Semana

**Prompt 1 — Crear el formulario:**
> "Crea hub/forms.py con ContactoForm (forms.Form): nombre (CharField), correo (EmailField), mensaje (CharField con Textarea). Agrega clase Bootstrap 'form-control' a cada widget."

**Prompt 2 — Vista con manejo POST:**
> "Crea la vista contacto que en GET muestre ContactoForm vacío y en POST valide, guarde Mensaje con cleaned_data, use messages.success y redirija a contacto."

**Prompt 3 — Configuración de producción:**
> "Modifica settings.py para leer SECRET_KEY y DEBUG desde .env con python-dotenv, define ALLOWED_HOSTS para PythonAnywhere y STATIC_ROOT para collectstatic."

**Prompt 4 — Error 403:**
> "Mi formulario Django da 403 al enviar. ¿Cuál es la causa más común y cómo la corrijo en la plantilla HTML?"
