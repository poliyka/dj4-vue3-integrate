from .settings import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.postgresql",
        "ENGINE": "psqlextra.backend",
        "OPTIONS": {"options": f"-c search_path={env('POSTGRES_SCHEMA')}"},
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Debug toolbar
MIDDLEWARE.insert(0,  'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS=('127.0.0.1', 'localhost')

# Print sql
MIDDLEWARE.extend(
    [
        "base.middleware.sql_middleware.SqlPrintingMiddleware",
    ]
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Django",
    "DESCRIPTION": "Your project description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
    "SWAGGER_UI_SETTINGS": {
        "url": "/api/schema",
    },
}

SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    # OTHER SETTINGS
}
