from django.urls import path

from api.version.v2 import views as custom_views

urlpatterns = [
    # system
    path("custom/myapi/", custom_views.MyApiView.as_view()),
]
