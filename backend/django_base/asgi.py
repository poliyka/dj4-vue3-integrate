"""
ASGI config for django_base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from pathlib import Path

import environ
from django.core.asgi import get_asgi_application

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    STRESS_TEST=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

environ.Env.read_env(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"django_base.settings.{env('DEV')}")

application = get_asgi_application()
