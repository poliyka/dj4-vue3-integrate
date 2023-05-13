from django.db import models
from django.utils.translation import gettext_lazy as _


class DateRangeChoices(models.TextChoices):
    DAY = "day", "Day"
    WEEK = "week", "Week"
    TWO_WEEK = "two_week", "Two week"
    MONTH = "month", "Month"
    THREE_MONTH = "three_month", "Three Month"
    YEAR = "year", "Year"


class I18nChoices(models.TextChoices):
    EN_US = "en-US", _("English")
    ZH_TW = "zh-TW", _("Traditional Chinese")
