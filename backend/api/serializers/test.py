from base.models import Profile
from django.contrib.auth.models import Permission, User
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Simple example",
            value={"hello": "01"},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Single param example",
            value={"hello": "data"},
            request_only=True,
            response_only=False,
        ),
    ]
)
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
