from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

ORDER = sorted((item, item) for item in ("asc", "desc"))


class PageQuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text="現在頁面", required=True, min_value=1)
    pageSize = serializers.IntegerField(help_text="頁面數量", required=True, min_value=1)
    sort = serializers.CharField(help_text="排序欄位", required=False, allow_blank=True)
    order = serializers.ChoiceField(choices=ORDER, default="desc", help_text="asc/desc")

class PageResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField(help_text="總筆數", required=True, min_value=0)
    next = serializers.CharField(help_text="下一頁", required=False, allow_blank=True)
    previous = serializers.CharField(help_text="上一頁", required=False, allow_blank=True)
    results = serializers.ListField(help_text="資料", child=serializers.JSONField(), allow_empty=True)


class ApiResponseSerializer(serializers.Serializer):
    code = serializers.CharField(help_text="回傳代碼")
    msg = serializers.CharField(help_text="回傳訊息")
    data = serializers.JSONField(help_text="回傳資料")
    fail = serializers.BooleanField(help_text="是否失敗")
    args = serializers.ListField(help_text="Other Args")
    kwargs = serializers.JSONField(help_text="Other Kwargs")


class VxeTableRecordSerializer(serializers.Serializer):
    insert_records = serializers.ListField(help_text="新增 Record", child=serializers.JSONField(), allow_empty=True)
    remove_records = serializers.ListField(help_text="刪除 Record", child=serializers.JSONField(), allow_empty=True)
    update_records = serializers.ListField(help_text="更新 Record", child=serializers.JSONField(), allow_empty=True)
