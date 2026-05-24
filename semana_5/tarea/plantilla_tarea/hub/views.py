# ============================================================
# SEMANA 5 — TAREA
#
# TAREA 1  → Completa la zona de personalización
# TAREA 2  → Lee y ejecuta la vista contacto() dada
# TAREA 3 → Personaliza el mensaje de éxito con tu nombre
# TAREA 4 → Sigue los pasos del README.md para desplegar
#                    en PythonAnywhere
#
# ENTREGA: URL pública de tu hub en PythonAnywhere.
# CRITERIO: El sitio carga en producción con tu información real.
# ============================================================

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recurso, Mensaje
from .forms import ContactoForm

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════
nombre_docente   = ""    # Tu nombre. Ej: "Prof. Ramírez"
materia          = ""    # Tu materia. Ej: "Educación Física"
institucion      = ""    # Tu institución
anos_experiencia = ""    # Años de experiencia
frase_mision     = ""    # Tu filosofía docente
# ════════════════════════════════════════════════════════════


def _ctx(extra=None):
    base = {'nombre_docente': nombre_docente, 'materia': materia, 'institucion': institucion}
    if extra:
        base.update(extra)
    return base


def inicio(request):
    return render(request, 'hub/inicio.html', _ctx({'frase_mision': frase_mision}))


def acerca(request):
    return render(request, 'hub/acerca.html', _ctx({'anos_experiencia': anos_experiencia, 'frase_mision': frase_mision}))


def recursos_view(request):
    return render(request, 'hub/recursos.html', _ctx({'recursos': Recurso.objects.all()}))


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            # ── TAREA 3: Personaliza este mensaje con tu nombre ──
            messages.success(request, '¡Tu mensaje fue enviado correctamente! Te responderé pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ContactoForm()
    return render(request, 'hub/contacto.html', _ctx({'form': form}))
