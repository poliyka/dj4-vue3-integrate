from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from base.models import Profile

admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name = "個人資料"
    verbose_name_plural = "個人資料"


class UserInlineAdmin(UserAdmin):
    inlines = [
        ProfileInline,
    ]


admin.site.register(User, UserInlineAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "birth",
        "gender",
        "identity",
        "address",
        "created_at",
        "updated_at",
    )
    search_fields = ["name"]
    raw_id_fields = ("user",)

    def view_name(self, obj):
        return obj.name