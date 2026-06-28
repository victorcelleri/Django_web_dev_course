from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recurso, Mensaje
from .forms import ContactoForm, ContactoFormEN

nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "10"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."


def inicio(request):
    return render(request, 'hub/inicio.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'frase_mision': frase_mision,
    })


def acerca(request):
    return render(request, 'hub/acerca.html', {
        'nombre_docente': nombre_docente,
        'materia': materia,
        'institucion': institucion,
        'anos_experiencia': anos_experiencia,
        'frase_mision': frase_mision,
    })


def recursos_view(request):
    recursos = Recurso.objects.all()
    return render(request, 'hub/recursos.html', {
        'nombre_docente': nombre_docente,
        'recursos': recursos,
    })


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(request, '¡Gracias! Tu mensaje fue recibido. Te responderé pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ContactoForm()
    return render(request, 'hub/contacto.html', {
        'nombre_docente': nombre_docente,
        'form': form,
    })


# ════════════════════════════════════════════════════════════
#  ENGLISH VIEWS  (/en/*)
# ════════════════════════════════════════════════════════════

def inicio_en(request):
    return render(request, 'hub/en/inicio.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'materia': 'Mathematics',
        'institucion': 'School Piquero',
        'frase_mision': 'Every student can master mathematics with the right guidance.',
    })


def about_en(request):
    return render(request, 'hub/en/acerca.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'materia': 'Mathematics',
        'institucion': 'School Piquero',
        'correo': 'prof.gonzalezsilva@school.edu',
        'anos_experiencia': anos_experiencia,
        'frase_mision': 'Every student can master mathematics with the right guidance.',
    })


def resources_en(request):
    from .models import Recurso
    return render(request, 'hub/en/recursos.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'recursos': Recurso.objects.all(),
    })


def contact_en(request):
    if request.method == 'POST':
        form = ContactoFormEN(request.POST)
        if form.is_valid():
            Mensaje.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(request, 'Thank you! Your message was received. I will get back to you soon.')
            return redirect('contacto_en')
        else:
            messages.error(request, 'Please fix the errors in the form.')
    else:
        form = ContactoFormEN()
    return render(request, 'hub/en/contacto.html', {
        'nombre_docente': 'Teacher Gonzalez Silva',
        'form': form,
    })

