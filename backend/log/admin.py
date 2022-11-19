from django.contrib import admin

from .models import Log


# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    # lsit display all fields exclude updated_at
    list_display = ("user", "method", "api", "action", "level", "message", "created_at")
    list_filter = ("action", "level", "created_at")
    search_fields = ("user", "class_", "api", "message")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
