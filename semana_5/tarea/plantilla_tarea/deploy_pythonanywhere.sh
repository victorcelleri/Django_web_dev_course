#!/bin/bash
# ============================================================
# DEPLOY — PythonAnywhere
# Ejecutar en la consola Bash de PythonAnywhere
# ============================================================
# 1. Configura tu usuario
#    export PA_USER="tuusuario"
# ============================================================

set -e

echo "============================================"
echo "  Despliegue del Hub Docente en PythonAnywhere"
echo "============================================"

# ── Configuración ──────────────────────────────────
PA_USER="${PA_USER:?Variable PA_USER no definida. Ej: export PA_USER=tuusuario}"
PA_REPO="Django_web_dev_course-main"
PA_PROJECT="semana_5/tarea/plantilla_tarea"
PA_HOME="/home/$PA_USER"
PA_PATH="$PA_HOME/$PA_REPO/$PA_PROJECT"

echo "Usuario:    $PA_USER"
echo "Ruta:       $PA_PATH"

# ── Paso 1: Ir al directorio del proyecto ──────────
cd "$PA_PATH"

# ── Paso 2: Crear .env a partir de .env.ejemplo ────
if [ ! -f .env ]; then
    cp .env.ejemplo .env
    echo ""
    echo "⚠️  Se creó .env. EDÍTALO con tus valores reales:"
    echo "   nano .env"
    echo ""
    echo "   SECRET_KEY=$(python3.10 -c 'import secrets; print(secrets.token_hex(32))')"
    echo "   DEBUG=False"
    echo "   ALLOWED_HOSTS=$PA_USER.pythonanywhere.com,localhost,127.0.0.1"
    echo ""
    read -p "Presiona Enter después de editar .env..."
fi

# ── Paso 3: Instalar dependencias ──────────────────
echo "Instalando dependencias..."
pip3.10 install --user -r requirements.txt

# ── Paso 4: Migraciones ────────────────────────────
echo "Ejecutando migraciones..."
python3.10 manage.py makemigrations hub
python3.10 manage.py migrate

# ── Paso 5: Recolectar estáticos ───────────────────
echo "Recolectando archivos estáticos..."
python3.10 manage.py collectstatic --noinput

# ── Paso 6: Crear superusuario ─────────────────────
echo ""
echo "¿Crear superusuario para /admin/? (s/n)"
read -r RESPUESTA
if [ "$RESPUESTA" = "s" ]; then
    python3.10 manage.py createsuperuser
fi

# ── Instrucciones finales ──────────────────────────
echo ""
echo "============================================"
echo "  ✅ INSTALACIÓN COMPLETADA"
echo "============================================"
echo ""
echo "Ahora ve a la pestaña Web de PythonAnywhere:"
echo ""
echo "  1. Add a new web app → Manual config → Python 3.10"
echo ""
echo "  2. Source code: $PA_PATH"
echo ""
echo "  3. WSGI file: Editar /var/www/${PA_USER}_pythonanywhere_com_wsgi.py"
echo "     Reemplazar TODO con el contenido de pythonanywhere_wsgi.py"
echo "     (Cambiar 'tuusuario' por '$PA_USER')"
echo ""
echo "  4. Static files:"
echo "     URL: /static/"
echo "     Directory: $PA_PATH/staticfiles"
echo ""
echo "  5. Haz clic en Reload"
echo ""
echo "  6. Abre: https://$PA_USER.pythonanywhere.com"
echo ""
