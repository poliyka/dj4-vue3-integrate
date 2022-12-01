import logging
from typing import Any

from api.version.v1.serializers.test import UserSerializer
from api.version.v1.serializers.user_data import UserDataSerializer
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.auth import get_user_model
from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger(__name__)

class UserDataApiView(APIView):
    authentication_classes = [JWTCookieAuthentication]
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

        current_user = User.objects.filter(id=request.user.id).first()
        user_data_serializer = UserDataSerializer(current_user)

        return JsonResponse(user_data_serializer.data, safe=True)

    # @extend_schema(
    #     tags=["System"],
    #     summary="UserDataPost",
    #     description="使用者資訊",
    #     responses={200: str, 401: str},
    #     request=UserSerializer,
    # )
    # @method_decorator(csrf_protect)
    # def post(self, request: HttpRequest, *args: Any, **kw: Any) -> JsonResponse:

    #     userSerializer = UserSerializer(data=request.data)

    #     if not userSerializer.is_valid():
    #         return JsonResponse(userSerializer.errors, status=HTTP_400_BAD_REQUEST)
    #     return JsonResponse(userSerializer.data, safe=True)
