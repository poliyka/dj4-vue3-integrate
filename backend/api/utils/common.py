import uuid
import datetime
import logging
import zoneinfo
from dataclasses import dataclass, field

# from dataclass_wizard import asdict
from datetime import timedelta
from enum import Enum, auto
from typing import Any

from api.code_handler import Code, getCodeMsg
from cron_converter import Cron
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Count, F, Func, OuterRef, Q, Subquery
from django.db.models.query import QuerySet
from django.utils import timezone
from log.models import Log


logger = logging.getLogger(__name__)

TZ_TW = zoneinfo.ZoneInfo(settings.TIME_ZONE)


def resMsg(
    code: Code,
    msg: str = "",
    data: dict | list | None = None,
    fail: bool = False,
    fmt: dict = {},
    *args,
    **kwargs,
):
    # 如果沒有 msg 就取得 Code 的 msg
    if not msg:
        msg = getCodeMsg(code, fmt)

    return {
        "code": code.value,
        "msg": msg,
        "data": data,
        "fail": fail,
        "args": args,
        "kwargs": kwargs,
    }


class JSONBUpdate(Func):
    def __init__(self, field, update):
        super().__init__(update)
        self.template = f"{field} || %(expressions)s"


# 記錄 Log
@dataclass
class LogRecord:
    method: str
    action: str
    level: str
    user: User | None = field(default=None, repr=False)
    api: str | None = field(default=None, repr=False)
    info: str | None = field(default=None, repr=False)
    message: str | None = field(default=None, repr=False)
    data: dict | list | None = field(default=None, repr=False)

    def save(self):
        Log.objects.create(
            method=self.method,
            action=self.action,
            level=self.level,
            user=self.user.username if self.user else None,
            api=self.api,
            info=self.info,
            message=self.message,
            data=self.data,
        )


def logRecord(
    method: str,
    action,
    level,
    user: User | None = None,
    api: str | None = None,
    info: str | None = None,
    message: str | None = None,
    data: dict | list | None = None,
):
    Log.objects.create(
        method=method,
        action=action,
        level=level,
        user=user.username if user else None,
        api=api,
        info=info,
        message=message,
        data=data,
    )


def prepare_order_by(data, qs):
    sort = data.get("sort")
    sort = sort.replace(".", "__") if sort else None
    order = data.get("order")
    if order and sort:
        qs = qs.order_by(f"{'-' if order == 'desc' else ''}{sort}")
    return qs


def msg_diff_field(origin, new, field, label=None):
    msg = ""
    if getattr(origin, field) != getattr(new, field):
        if label:
            msg += f"{label}: "
        else:
            msg += f"{field}: "
        return msg + f"{getattr(origin, field)} => {getattr(new, field)}\n"
    return msg
