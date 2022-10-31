from .settings import *

MIDDLEWARE.extend(
    [
        "base.middleware.sql_middleware.SqlPrintingMiddleware",
    ]
)

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
