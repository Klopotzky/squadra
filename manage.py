#!/usr/bin/env python
<<<<<<< HEAD

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squadra_main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
=======
import os
from aldryn_django import startup


if __name__ == "__main__":
    startup.manage(path=os.path.dirname(os.path.abspath(__file__)))
>>>>>>> 8df0496d07d81875516d9350a867ae7830143c26
