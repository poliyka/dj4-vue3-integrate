from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         # "ENGINE": "django.db.backends.postgresql",
#         "ENGINE": "psqlextra.backend",
#         "OPTIONS": {"options": f"-c search_path={env('POSTGRES_SCHEMA')},public"},
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("POSTGRES_HOST"),
#         "PORT": env("POSTGRES_PORT"),
#     }
# }

INSTALLED_APPS.extend(["debug_toolbar", "django_extensions"])

# Debug toolbar
INTERNAL_IPS = ("127.0.0.1", "localhost")

MIDDLEWARE.extend(
    [
        # Print sql
        # "base.middleware.sql_middleware.SqlPrintingMiddleware",
        # "base.middleware.sql_middleware.ApiPrintingMiddleware",
        # disable csrf token
        "base.middleware.disable_csrftoken_middleware.DisableCSRFOnDev",
    ]
)
