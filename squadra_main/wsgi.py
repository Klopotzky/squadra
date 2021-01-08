"""
WSGI config for squadra_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
# from aldryn_django import startup
# import startup as startup
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'squadra_main.settings')

application = get_wsgi_application()

# application = startup.wsgi(path=os.path.dirname(__file__))