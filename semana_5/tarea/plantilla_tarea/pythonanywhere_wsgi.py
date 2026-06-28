"""
WSGI para PythonAnywhere
─────────────────────────
Pega TODO este contenido en el archivo WSGI de la pestaña Web:
  /var/www/tuusuario_pythonanywhere_com_wsgi.py

Cambia 'tuusuario' por tu nombre de usuario real.
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# ─── CAMBIA esto por tu usuario de PythonAnywhere ───
PA_USER = "tuusuario"
# ─────────────────────────────────────────────────────

path = f'/home/{PA_USER}/Django_web_dev_course-main/semana_5/tarea/plantilla_tarea'
if path not in sys.path:
    sys.path.insert(0, path)

# Cargar .env con ruta absoluta
load_dotenv(os.path.join(path, '.env'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'hub_docente.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
