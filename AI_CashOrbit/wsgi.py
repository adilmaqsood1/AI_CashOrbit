"""
WSGI config for AI_CashOrbit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Directly set the settings module without using os.environ.setdefault
os.environ['DJANGO_SETTINGS_MODULE'] = 'AI_CashOrbit.settings_production'

application = get_wsgi_application()
