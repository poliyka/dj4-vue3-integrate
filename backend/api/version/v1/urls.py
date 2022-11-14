from django.urls import path

from .views import UserDataApiView

urlpatterns = [
    path("user-data/", UserDataApiView.as_view(), name="user_data"),
]
