from base.models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers

# https://github.com/axnsan12/drf-yasg/blob/master/testproj/snippets/serializers.py#L48

##################
# 使用者基本資訊 #
##################
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar", "birth", "gender")


class UserDataSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "is_active",
            "user_permissions",
            "groups",
            "date_joined",
            "is_staff",
            "is_superuser",
        )
