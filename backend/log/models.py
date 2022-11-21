from base.models import BaseTimeModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from websocket.utils import retrieve_log_data, channels_control_message
from typing import Any


class Log(BaseTimeModel):
    """Log model"""

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
        "Api路徑",
        max_length=32,
        blank=True,
        null=True,
        help_text="api path like '/api/v1/xxx'",
    )
    action = models.CharField("執行操作", max_length=16, choices=Action.choices, default=Action.SYSTEM)
    level = models.CharField("等級", max_length=8, choices=Level.choices, default=Level.INFO)
    message = models.TextField("訊息", blank=True, null=True)

    # On Save event
    def save(self, *args: Any, **kwargs: Any) -> Any:
        res = super().save(*args, **kwargs)
        channels_control_message(
            "log",
            {
                "id": self.id,
                "user": self.user,
                "method": self.method,
                "api": self.api,
                "action": self.action,
                "level": self.level,
                "message": self.message,
            },
        )
        return res

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"[{self.level}]{self.message}"
