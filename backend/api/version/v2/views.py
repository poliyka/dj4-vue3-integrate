import logging
from typing import Any

from api.code_handler import Code
from api.utils.common import resMsg
from api.version.v1.serializers.user_data_serializer import UserDataSerializer
from api.version.v2.serializers import MySerializer, MySerializerRes, MySerializerRes1
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpRequest
from drf_spectacular.utils import OpenApiResponse, extend_schema

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import status as Status_code
from rest_framework.generics import GenericAPIView

# from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.version.v2.filters.system_filter import MyFilter

logger = logging.getLogger(__name__)


class MyApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Custom"],
        summary="MyApiGet",
        responses={200: str, 401: str},
        parameters=[MySerializer],
    )
    def get(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        res = request.query_params
        # 建立物件
        ser = MySerializer(data=res)
        # 驗證
        ser.is_valid(raise_exception=True)
        # 取得驗證後的 data
        data = ser.data
        return Response({"res": res})

    @extend_schema(
        tags=["Custom"],
        summary="MyApiPost",
        responses={200: MySerializerRes(many=True), 401: str},
        request=MySerializer,
    )
    def post(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        res = request.data
        # 建立物件
        ser = MySerializer(data=res)
        # 驗證
        ser.is_valid(raise_exception=True)
        # 取得驗證後的 data
        data = ser.data
        print(data)

        # 用 Filter 查詢
        qt = MyFilter(data=data).qs
        print(qt)

        # 使用 Response Serializer parser Queryset data
        res_data = MySerializerRes(qt, many=True)

        return Response(res_data.data)

    @extend_schema(
        tags=["Custom"],
        summary="MyApiPostFullName",
        responses={200: MySerializerRes1, 401: str},
        request=MySerializer,
    )
    def patch(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        res = request.data
        # 建立物件
        ser = MySerializer(data=res)
        # 驗證
        ser.is_valid(raise_exception=True)
        # 取得驗證後的 data
        data = ser.data

        user_qs = User.objects.filter(username__icontains=data.get("param", None))

        res_json = [{"abc": "name", "efg": "123", "cccc": 12312}, {"abc": "name", "efg": "123", "cccc": 12312}]

        res_data = MySerializerRes1(res_json, many=True)
        # res_data = MySerializerRes1(user_qs, many=True)

        return Response(res_data.data)
