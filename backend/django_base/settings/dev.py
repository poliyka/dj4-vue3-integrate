from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if env("DATABASE_URL", default=None):
    DATABASES = {
        "default": env.db(),
    }
else:
    DATABASES = {
        "default": {
            # "ENGINE": "django.db.backends.postgresql",
            "ENGINE": "psqlextra.backend",
            "OPTIONS": {"options": f"-c search_path={env('POSTGRES_SCHEMA')},public"},
            "NAME": env("POSTGRES_DB"),
            "USER": env("POSTGRES_USER"),
            "PASSWORD": env("POSTGRES_PASSWORD"),
            "HOST": env("POSTGRES_HOST"),
            "PORT": env("POSTGRES_PORT"),
        }
    }

# APP
INSTALLED_APPS.extend(["debug_toolbar", "django_extensions"])

# Debug toolbar
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = ("127.0.0.1", "localhost")

MIDDLEWARE.extend(
    [
        # Print sql
        # "base.middleware.sql_middleware.SqlPrintingMiddleware",
        "base.middleware.sql_middleware.ApiPrintingMiddleware",
        # disable csrf token
        "base.middleware.disable_csrftoken_middleware.DisableCSRFOnDev",
    ]
)

# schema 圖表化設定
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Dj4-swagger",
    "DESCRIPTION": "Dev",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
    "SWAGGER_UI_SETTINGS": {
        "url": "/api/schema",
    },
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "COMPONENT_SPLIT_REQUEST": True,
}
