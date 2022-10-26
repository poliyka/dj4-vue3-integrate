from rest_framework import serializers
from base.models import Profile
from django.contrib.auth.models import Permission, User

# https://github.com/axnsan12/drf-yasg/blob/master/testproj/snippets/serializers.py#L48

##################
# 使用者基本資訊 #
##################
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name", "codename")

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ("id", "user", "created_at")

class UserDataSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        exclude = ("password", "first_name", "last_name", "last_login", "is_active", "user_permissions", "groups")
