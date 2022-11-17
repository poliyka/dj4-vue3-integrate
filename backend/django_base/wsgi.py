"""
WSGI config for django_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

import environ
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"django_base.settings.{env('DEV')}")

application = get_wsgi_application()
