"""
WSGI config for django_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEV = os.environ.get("DEV")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"django_base.settings.{DEV}")

application = get_wsgi_application()
