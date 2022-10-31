import django.utils.timezone as timezone
from django.contrib.auth.models import Group, Permission, User
from django.db import models
from django.db.models import Sum


class BaseTimeModel(models.Model):
    """Timestamp interface model"""

    created_at = models.DateTimeField("建立時間", auto_now_add=True)
    updated_at = models.DateTimeField("最後更新時間", auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseTimeModel):
    """使用者個人資料"""

    class Gender(models.TextChoices):
        MALE = "male", "男"
        FEMALE = "female", "女"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar
    avatar = models.ImageField(
        verbose_name="大頭照",
        upload_to="avatar/%Y-%m-%d/",
        blank=True,
        null=True,
    )

    # information
    name = models.CharField("姓名", max_length=32, blank=True, null=True)
    birth = models.DateField("生日", blank=True, null=True)
    gender = models.CharField("性別", max_length=16, choices=Gender.choices, blank=True, null=True)
    identity = models.CharField("身分證字號", max_length=16, blank=True, null=True, unique=True)
    tel = models.CharField("住家電話", max_length=16, blank=True, null=True)
    mobile = models.CharField("行動電話", max_length=32, blank=True, null=True)
    address = models.CharField("聯絡地址", max_length=256, blank=True, null=True)
    note = models.TextField("備註", blank=True, null=True)

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"{self.user.username}/{self.user.__str__()}"
