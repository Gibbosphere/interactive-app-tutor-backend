#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

    # Get the port from the .env file, defaulting to 8085 if not set
    port = config('DJANGO_PORT', default='8085')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Modify the arguments if runserver is used and no port is explicitly passed
    if 'runserver' in sys.argv and len(sys.argv) == 2:
        sys.argv.append(f'0.0.0.0:{port}')
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
