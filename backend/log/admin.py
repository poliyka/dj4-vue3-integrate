from django.contrib import admin

from .models import Log


# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("user", "method", "api", "action", "level", "message", "created")
    list_filter = ("action", "level", "created")
    search_fields = ("user", "class_", "api", "message")
    ordering = ("-created",)
    readonly_fields = ("created",)
