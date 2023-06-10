from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = "api"

urlpatterns = [
    # rest auth
    path("accounts/", include("dj_rest_auth.urls")),
    # path("accounts/registration/", include("dj_rest_auth.registration.urls")),
    # v1
    path("v1/", include("api.version.v1.urls"), name="v1"),
    path("v2/", include("api.version.v2.urls"), name="v2"),
]


if settings.DEV in ["dev", "stage"]:
    # swagger
    urlpatterns.extend(
        [
            path("schema/", SpectacularAPIView.as_view(), name="schema"),
            path(
                "swagger/",
                SpectacularSwaggerView.as_view(url_name="api:schema"),
                name="swagger",
            ),
            path(
                "redoc/",
                SpectacularRedocView.as_view(url_name="api:schema"),
                name="redoc",
            ),
        ]
    )
