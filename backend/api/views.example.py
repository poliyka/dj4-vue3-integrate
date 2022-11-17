import json
import logging
from typing import Any

from api.version.v1.serializers.test import UserSerializer
from api.version.v1.serializers.user_data import UserDataSerializer
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Max
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.decorators import APIView, action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_406_NOT_ACCEPTABLE,
)


class UserDataApiView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    @extend_schema(
        tags=["System"],
        summary="UserData",
        description="使用者資訊",
        responses={200: str, 401: str},
    )
    def get(self, request: HttpRequest, *args: Any, **kw: Any) -> JsonResponse:
        User = get_user_model()
        # flash query prevent cache user
        current_user = User.objects.filter(id=request.user.id).first()
        user_data_serializer = UserDataSerializer(current_user)

        return JsonResponse(user_data_serializer.data, safe=True)

    @extend_schema(
        tags=["System"],
        summary="UserDataPost",
        description="使用者資訊",
        responses={200: str, 401: str},
        request=UserSerializer,
    )
    @method_decorator(csrf_protect)
    def post(self, request: HttpRequest, *args: Any, **kw: Any) -> JsonResponse:

        userSerializer = UserSerializer(data=request.data)

        if not userSerializer.is_valid():
            return JsonResponse(userSerializer.errors, status=HTTP_400_BAD_REQUEST)
        return JsonResponse(userSerializer.data, safe=True)
