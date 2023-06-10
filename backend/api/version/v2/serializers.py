from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Profile


class MySerializer(serializers.Serializer):
    username_fed = serializers.CharField(help_text="username_fed", required=False)
    first_name_fed = serializers.CharField(help_text="first_name_fed", required=False)
    gender_fed = serializers.ListField(
        help_text="gender_fed", required=False, child=serializers.ChoiceField(choices=Profile.Gender.choices)
    )
    created_after = serializers.DateTimeField(help_text="created_after", required=False)
    created_before = serializers.DateTimeField(help_text="created_before", required=False)

class MySerializerRes(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")


class MySerializerRes1(serializers.Serializer):
    abc = serializers.CharField(help_text="abc", required=True)
    efg = serializers.IntegerField(help_text="efg", required=True)
    # full_name = serializers.SerializerMethodField()

    # def get_full_name(self, user):
    #     return {"username": user.username, "full_name": user.first_name + user.last_name}
