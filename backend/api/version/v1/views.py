import copy
import logging
import re
from typing import Any

from api.code_handler import Code
from api.decorators.api_handler import ErrorHandler
from api.decorators.permission_helper import PermissionAllow
from api.filters.system_filters import UserListFilter
from api.serializers.system import (
    HistoryLogResponseSerializer,
    HistoryLogSerializer,
    UserListQuerySerializer,
    V1UserListResponseSerializer,
)
from api.serializers.utils import ApiResponseSerializer
from api.utils.common import msg_diff_field, prepare_order_by, resMsg
from api.version.v1.filters.system_filter import HistoryLogFilter
from api.version.v1.forms.user_data_form import ProfileAvatarForm
from api.version.v1.serializers.user_data_serializer import (
    CreateAccountQuerySerializer,
    HistoryLogQuerySerializer,
    ProfileAvatarQuerySerializer,
    ProfilePatchSerializer,
    SetAccountPassQuerySerializer,
    UpdateAccountQuerySerializer,
    UserDataSerializer,
    UserPatchSerializer,
    UserProfilePatchQuerySerializer,
)
from base.forms.auth import CustomSetPasswordForm, CustomSignupForm
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from drf_spectacular.utils import OpenApiResponse, extend_schema
from log.models import Log

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import status as Status_code
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

# from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rolepermissions.permissions import available_perm_status, grant_permission, revoke_permission

logger = logging.getLogger(__name__)


class UserDataApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="取得使用者資訊",
        responses={200: str, 401: str},
    )
    def get(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        User = get_user_model()
        if not request.user.is_authenticated:
            return Response(
                resMsg(Code.HTTP_401_UNAUTHORIZED, fail=True),
                status=Status_code.HTTP_401_UNAUTHORIZED,
            )

        current_user = User.objects.filter(id=request.user.id).first()
        user_data_serializer = UserDataSerializer(current_user)

        return Response(user_data_serializer.data)


class UserListApiView(GenericAPIView):
    # pagination
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = "pageSize"
    pagination_class.page_size = 10
    # authentication permission
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, query_data) -> Any:
        """query data by PageNumberPagination"""

        filtered_qs = UserListFilter(self.request.query_params).qs
        filtered_qs = prepare_order_by(query_data, filtered_qs)

        return self.paginate_queryset(filtered_qs)

    @extend_schema(
        tags=["System"],
        summary="使用者列表",
        responses={
            200: V1UserListResponseSerializer,
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        parameters=[UserListQuerySerializer],
    )
    @method_decorator(PermissionAllow(allows=["Admin", "Maintainer"]))
    def get(self, request, *args: Any, **kw: Any) -> Response:
        # valid params
        query_serializer = UserListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        # query data
        queryset = self.get_queryset(query_data)
        data_serializer = UserDataSerializer(queryset, many=True)
        return self.get_paginated_response(data_serializer.data)


class UserProfileApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="更新使用者部分資訊",
        responses={
            201: OpenApiResponse(description="Profile is up to date!, But no return"),
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=UserProfilePatchQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["__all__"]))
    @method_decorator(csrf_protect)
    def patch(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        # 檢查 data 是否正確
        query_serializer = UserProfilePatchQuerySerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        # 分別取得 user 與 profile 資料
        user_data = query_data.get("user", {})
        profile_data = query_data.get("profile", {})

        # 取得使用者資料
        current_user = User.objects.filter(id=request.user.id).first()

        # 更新資料
        user_serializer = UserPatchSerializer(current_user, data=user_data, partial=True)
        profile_serializer = ProfilePatchSerializer(current_user.profile, data=profile_data, partial=True)

        user_serializer.is_valid(raise_exception=True)
        profile_serializer.is_valid(raise_exception=True)

        user_serializer.save()
        profile_serializer.save()

        return Response(
            resMsg(
                Code.SUCCESS_NO_RESPONSE,
                data={"user": user_serializer.data, "profile": profile_serializer.data},
            ),
            status=Status_code.HTTP_201_CREATED,
        )


class ProfileAvatarApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="更新使用者大頭貼",
        responses={
            201: OpenApiResponse(description="Image is up to date!, But no return"),
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=ProfileAvatarQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["__all__"]))
    @method_decorator(csrf_protect)
    def patch(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        try:
            # 取得使用者資料
            current_user = User.objects.get(id=request.user.id)

            form = ProfileAvatarForm(instance=current_user.profile, data=request.data, files=request.FILES)
            if not form.is_valid():
                res_data = resMsg(Code.HTTP_500_INTERNAL_SERVER_ERROR, data=form.errors, fail=True)
                return Response(res_data)

            form.save()
        except:
            return Response(resMsg(Code.HTTP_500_INTERNAL_SERVER_ERROR, fail=True))

        return Response(resMsg(Code.SUCCESS_NO_RESPONSE))

    @extend_schema(
        tags=["System"],
        summary="移除使用者大頭貼",
        responses={
            201: OpenApiResponse(description="Image is Delete!"),
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=ProfileAvatarQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["__all__"]))
    @method_decorator(csrf_protect)
    def delete(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        try:
            # 取得使用者資料
            current_user = User.objects.get(id=request.user.id)

            # 刪除大頭照
            current_user.profile.avatar.delete()
        except:
            return Response(resMsg(Code.HTTP_500_INTERNAL_SERVER_ERROR, fail=True))

        return Response(resMsg(Code.SUCCESS_NO_RESPONSE))


class CreateAccountApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="新增使用者與權限",
        responses={
            200: ApiResponseSerializer,
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=CreateAccountQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["Admin"]))
    @method_decorator(csrf_protect)
    def post(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        # 檢查 data 是否正確
        query_serializer = CreateAccountQuerySerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        # attr
        username = query_data.get("username", "")

        # check user is exists
        user = User.objects.filter(username=username)
        if user.exists():
            return Response(resMsg(Code.USER_IS_EXISTS, fail=True))

        # Create Form for validate
        form = CustomSignupForm(request.data)

        # validate form
        if not form.is_valid():
            res_data = resMsg(Code.FORM_DATA_IS_NOT_VALID, data=form.errors, fail=True)
            return Response(res_data)

        @ErrorHandler("Create new user", Log.Action.JOB, Log.Level.ERROR, data=query_data)
        def main(log) -> dict:
            form.save(request)
            log.message = f"New user '{username}' created"

            return resMsg(Code.SUCCESS_NO_RESPONSE)

        res_msg = main(self)
        return Response(res_msg)


class UpdateAccountApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="更新使用者資料與權限",
        responses={
            200: ApiResponseSerializer,
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=UpdateAccountQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["Admin"]))
    @method_decorator(csrf_protect)
    def post(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        # 檢查 data 是否正確
        query_serializer = UpdateAccountQuerySerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        # attr
        data = query_data.get("data", [])
        for d in data:
            username = d.get("username", "")
            first_name = d.get("first_name", "")
            last_name = d.get("last_name", "")
            email = d.get("email", "")
            permissions = d.get("permissions", {})
            is_active = d.get("is_active", True)

            # check email is exists
            email_chk_qs = User.objects.filter(email=email).exclude(username=username)
            if email_chk_qs.exists():
                res_data = resMsg(Code.USER_EMAIL_IS_EXISTS, fail=True, fmt={"email": email})
                return Response(res_data)

            @ErrorHandler(
                "Update user profile and permissions",
                Log.Action.SYSTEM,
                Log.Level.ERROR,
                data=d,
            )
            def main(log) -> dict:
                # update user info
                user = User.objects.get(username=username)
                origin_user = copy.deepcopy(user)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.is_active = is_active
                user.save()

                # log data
                log.message = f"Account: {username} \n"
                log.message += msg_diff_field(origin_user, user, "first_name", "First Name")
                log.message += msg_diff_field(origin_user, user, "last_name", "Last Name")
                log.message += msg_diff_field(origin_user, user, "email", "Email")
                log.message += msg_diff_field(origin_user, user, "is_active", "Active")

                # update role
                av_perms = available_perm_status(user)
                for perm_key, perm_value in permissions.items():
                    if perm_value and av_perms.get(perm_key) != perm_value:
                        grant_permission(user, perm_key)
                        log.message += f"Grant '{perm_key}' permission\n"
                    elif not perm_value and av_perms.get(perm_key) != perm_value:
                        revoke_permission(user, perm_key)
                        log.message += f"Revoke '{perm_key}' permission\n"

                return resMsg(Code.SUCCESS_NO_RESPONSE)

            res_msg = main(self)

        return Response(res_msg)


class SetAccountPasswordApiView(GenericAPIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["System"],
        summary="更新使用者密碼",
        responses={
            200: ApiResponseSerializer,
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        request=SetAccountPassQuerySerializer,
    )
    @method_decorator(PermissionAllow(allows=["Admin"]))
    @method_decorator(csrf_protect)
    def post(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        # 檢查 data 是否正確
        query_serializer = SetAccountPassQuerySerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        # check user is exists
        username = query_data.get("username", "")
        user_qs = User.objects.filter(username=username)
        if not user_qs.exists():
            res_data = resMsg(Code.HTTP_500_INTERNAL_SERVER_ERROR, fail=True)
            return Response(res_data)

        # check password
        form = CustomSetPasswordForm(user_qs.first(), request.data)
        if not form.is_valid():
            res_data = resMsg(Code.FORM_DATA_IS_NOT_VALID, data=form.errors, fail=True)
            return Response(res_data)

        @ErrorHandler(
            "Update user password",
            Log.Action.SYSTEM,
            Log.Level.ERROR,
        )
        def main(log) -> dict:
            form.save()

            # 紀錄 log
            password = query_data.get("password1", "")
            password = re.sub(r"^.{0,5}", "*****", password)
            log.message = (f"Account: {username}\nNew Password: {password}",)

            return resMsg(Code.SUCCESS_NO_RESPONSE)

        res_msg = main(self)

        return Response(res_msg)


class GetHistoryLogApiView(GenericAPIView):
    # pagination
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = "pageSize"
    pagination_class.page_size = 10
    # authentication permission
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, query_data) -> Any:
        """query data by PageNumberPagination"""

        filtered_qs = HistoryLogFilter(data=query_data).qs
        filtered_qs = prepare_order_by(query_data, filtered_qs)

        return self.paginate_queryset(filtered_qs)

    @extend_schema(
        tags=["System"],
        summary="取得歷史紀錄",
        responses={
            200: HistoryLogResponseSerializer,
            400: OpenApiResponse(description="Bad request (something invalid)"),
        },
        parameters=[HistoryLogQuerySerializer],
    )
    @method_decorator(PermissionAllow(allows=["Admin", "Maintainer"]))
    def get(self, request: HttpRequest, *args: Any, **kw: Any) -> Response:
        query_serializer = HistoryLogQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        query_data = query_serializer.data

        queryset = self.get_queryset(query_data)
        data_serializer = HistoryLogSerializer(queryset, many=True)

        return self.get_paginated_response(data_serializer.data)
