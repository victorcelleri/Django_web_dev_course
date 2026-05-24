#!/usr/bin/env python
"""Django command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hub_docente.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Verifica que esté instalado: pip install django"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
