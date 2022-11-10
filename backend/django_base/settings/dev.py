from .settings import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.db(),
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

# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    "http://127.0.0.1:9000",
    "http://localhost:9000",
)
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "VIEW",
)
CORS_ALLOW_HEADERS = [
    "XMLHttpRequest",
    "X_FILENAME",
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# schema 圖表化設定
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

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
