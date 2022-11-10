from base.models import BaseTimeModel
from django.db import models
from django.utils.translation import gettext_lazy as _

from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel
from psqlextra.manager import PostgresManager


class Log(PostgresPartitionedModel, BaseTimeModel):
    """Log model"""

    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["created_at"]

    objects = PostgresManager()

    class Level(models.TextChoices):
        DEBUG = "debug", _("Debug")
        INFO = "info", _("Info")
        WARNING = "warning", _("Warning")
        ERROR = "error", _("Error")
        CRITICAL = "critical", _("Critical")

    class Action(models.TextChoices):
        SYSTEM = "system", _("System")
        LOGIN = "login", _("Login")
        LOGOUT = "logout", _("Logout")

    user = models.CharField("使用者", max_length=32, blank=True, null=True)
    method = models.CharField(
        "方法名稱", max_length=32, help_text="func or class name like 'Login.as_view()'"
    )
    api = models.CharField(
        "Api路徑", max_length=32, blank=True, null=True, help_text="api path like '/api/v1/xxx'"
    )
    action = models.CharField("執行操作", max_length=16, choices=Action.choices, default=Action.SYSTEM)
    level = models.CharField("等級", max_length=8, choices=Level.choices, default=Level.INFO)
    message = models.TextField("訊息", blank=True, null=True)

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"[{self.level}] {self.method}"
