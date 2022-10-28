"""
ASGI config for django_base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

import environ
from django.core.asgi import get_asgi_application

env = environ.Env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"django_base.settings.{env('DEV')}")

application = get_asgi_application()
