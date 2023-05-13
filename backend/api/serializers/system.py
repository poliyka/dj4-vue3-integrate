from api.serializers.utils import PageQuerySerializer, PageResponseSerializer
from api.version.v1.serializers.user_data_serializer import (
    UserDataSerializer as V1UserDataSerializer,
)
from log.models import Log
from rest_framework import serializers


class UserListQuerySerializer(PageQuerySerializer):
    account = serializers.CharField(help_text="帳號", required=False, allow_null=True, allow_blank=True)
    name = serializers.CharField(help_text="名稱", required=False, allow_null=True, allow_blank=True)
    email = serializers.CharField(help_text="信箱", required=False, allow_null=True, allow_blank=True)
    is_active = serializers.BooleanField(help_text="是否啟用", required=False, allow_null=True)


class V1UserListResponseSerializer(PageResponseSerializer):
    results = serializers.ListField(help_text="資料", child=V1UserDataSerializer(), allow_empty=True)


class HistoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ("data",)


class HistoryLogResponseSerializer(PageResponseSerializer):
    results = serializers.ListField(help_text="資料", child=HistoryLogSerializer(), allow_empty=True)
