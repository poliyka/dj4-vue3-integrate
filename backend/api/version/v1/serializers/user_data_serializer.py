from api.serializers.utils import PageQuerySerializer
from base.choices import I18nChoices
from base.models import Profile
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rolepermissions.permissions import available_perm_status

# https://github.com/axnsan12/drf-yasg/blob/master/testproj/snippets/serializers.py#L48


##################
# 使用者基本資訊 #
##################
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("id", "user", "created", "modified")


class UserDataSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    permissions = serializers.SerializerMethodField()

    @extend_schema_field(serializers.JSONField)
    def get_permissions(self, user):
        return available_perm_status(user)

    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "user_permissions",
            "groups",
            "is_staff",
            "is_superuser",
        )


class UserPatchQuerySerializer(serializers.Serializer):
    first_name = serializers.CharField(
        help_text="名", required=False, allow_null=True, allow_blank=True
    )
    last_name = serializers.CharField(
        help_text="姓", required=False, allow_null=True, allow_blank=True
    )
    email = serializers.CharField(help_text="信箱", required=True)


class ProfilePatchQuerySerializer(serializers.Serializer):
    title = serializers.CharField(
        help_text="職稱", required=False, allow_null=True, allow_blank=True
    )
    gender = serializers.ChoiceField(
        help_text="性別",
        choices=Profile.Gender.choices,
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    tel = serializers.CharField(
        help_text="公司電話", required=False, allow_null=True, allow_blank=True
    )
    tel_ext = serializers.CharField(
        help_text="分機", required=False, allow_null=True, allow_blank=True
    )
    mobile = serializers.CharField(
        help_text="行動電話", required=False, allow_null=True, allow_blank=True
    )
    theme_dark = serializers.BooleanField(help_text="深色主題", required=True)
    language = serializers.ChoiceField(
        help_text="語系", choices=I18nChoices.choices, required=True
    )


class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfilePatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "title",
            "gender",
            "tel",
            "tel_ext",
            "mobile",
            "theme_dark",
            "language",
        )


class UserProfilePatchQuerySerializer(serializers.Serializer):
    user = UserPatchQuerySerializer()
    profile = ProfilePatchQuerySerializer()


class ProfileAvatarQuerySerializer(serializers.Serializer):
    avatar = serializers.ImageField(help_text="頭像", required=True)


class CreateAccountQuerySerializer(serializers.Serializer):
    username = serializers.CharField(help_text="帳號", required=True)
    password = serializers.CharField(help_text="密碼", required=True)
    password1 = serializers.CharField(help_text="確認密碼", required=True)
    first_name = serializers.CharField(
        help_text="名", required=False, allow_null=True, allow_blank=True
    )
    last_name = serializers.CharField(
        help_text="姓", required=False, allow_null=True, allow_blank=True
    )
    email = serializers.CharField(help_text="信箱", required=True)
    permissions = serializers.ListField(
        help_text="權限", child=serializers.CharField(), required=True
    )


class updateAccountPermissionsSerializer(serializers.Serializer):
    Admin = serializers.BooleanField(help_text="Admin", required=False)
    Maintainer = serializers.BooleanField(help_text="Maintainer", required=False)
    Developer = serializers.BooleanField(help_text="Developer", required=False)
    Viewer = serializers.BooleanField(help_text="Viewer", required=False)


class UpdateAccountDataSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="帳號", required=True)
    first_name = serializers.CharField(
        help_text="名", required=False, allow_null=True, allow_blank=True
    )
    last_name = serializers.CharField(
        help_text="姓", required=False, allow_null=True, allow_blank=True
    )
    email = serializers.CharField(help_text="信箱", required=True)
    permissions = updateAccountPermissionsSerializer(help_text="權限", required=True)
    is_active = serializers.BooleanField(help_text="是否啟用", required=True)


class UpdateAccountQuerySerializer(serializers.Serializer):
    data = serializers.ListField(
        help_text="人員資料", child=UpdateAccountDataSerializer(), required=True
    )


class SetAccountPassQuerySerializer(serializers.Serializer):
    username = serializers.CharField(help_text="帳號", required=True)
    password1 = serializers.CharField(help_text="密碼", required=True)
    password2 = serializers.CharField(help_text="確認密碼", required=True)


class HistoryLogQuerySerializer(PageQuerySerializer):
    user = serializers.CharField(help_text="User", required=False)
    method = serializers.CharField(help_text="Method", required=False)
    action = serializers.ListField(
        help_text="Action",
        child=serializers.CharField(trim_whitespace=False),
        required=False,
    )
    level = serializers.ListField(
        help_text="Level",
        child=serializers.CharField(trim_whitespace=False),
        required=False,
    )
    info = serializers.CharField(help_text="Info", required=False)
    created_after = serializers.DateTimeField(help_text="Created >= ", required=False)
    created_before = serializers.DateTimeField(help_text="Created <= ", required=False)
