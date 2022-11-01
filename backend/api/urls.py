from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from .views import UserDataApiView

app_name = "api"

urlpatterns = [
    # rest auth
    path("v1/accounts/", include("dj_rest_auth.urls"), name="accounts"),
    path(
        "v1/accounts/registration/",
        include("dj_rest_auth.registration.urls"),
        name="registration",
    ),
    # v1
    path("v1/user-data/", UserDataApiView.as_view(), name="user-data"),
]

if settings.DEV in ["dev", "stage"]:
    urlpatterns.extend(
        [
            # YOUR PATTERNS
            path("schema/", SpectacularAPIView.as_view(), name="schema"),
            # Optional UI:
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
