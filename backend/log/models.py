from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

class Log(TimeStampedModel):
    """Log model"""

    class Level(models.TextChoices):
        DEBUG = "debug", "Debug"
        INFO = "info", "Info"
        WARNING = "warning", "Warning"
        ERROR = "error", "Error"
        CRITICAL = "critical", "Critical"

    class Action(models.TextChoices):
        SYSTEM = "system", "System"
        LOGIN = "login", "Login"
        LOGOUT = "logout", "Logout"
        SIGNUP = "signup", "Signup"
        DASHBOARD = "dashboard", "Dashboard"
        SCHEDULE = "schedule", "Schedule"
        SERVICE = "service", "Service"
        JOB = "job", "Job"

    user = models.CharField("使用者", max_length=64, blank=True, null=True)
    method = models.CharField("方法名稱", max_length=64, help_text="func or class name like 'ClassName/func_name'")
    api = models.CharField(
        "Api路徑",
        max_length=256,
        blank=True,
        null=True,
        help_text="api path like '/api/v1/xxx/'",
    )
    action = models.CharField("執行操作", max_length=16, choices=Action.choices, default=Action.SYSTEM)
    level = models.CharField("等級", max_length=16, choices=Level.choices, default=Level.INFO)
    info = models.CharField("訊息", max_length=128, blank=True, null=True)
    message = models.TextField("詳細訊息", blank=True, null=True)
    data = models.JSONField("資料", blank=True, null=True)

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"[{self.level}] {self.method}"
