from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel
from base.choices import I18nChoices

# Unique email
User._meta.get_field("email")._unique = True


class Profile(TimeStampedModel):
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
    title = models.CharField("職稱", max_length=32, blank=True, null=True)
    gender = models.CharField("性別", max_length=16, choices=Gender.choices, blank=True, null=True)
    tel = models.CharField("公司電話", max_length=16, blank=True, null=True)
    tel_ext = models.CharField("分機", max_length=16, blank=True, null=True)
    mobile = models.CharField("行動電話", max_length=32, blank=True, null=True)

    # preferences
    theme_dark = models.BooleanField("深色主題", default=True)
    language = models.CharField("語言", max_length=16, choices=I18nChoices.choices, default=I18nChoices.ZH_TW)

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"{self.user.username}/{self.user.__str__()}"
