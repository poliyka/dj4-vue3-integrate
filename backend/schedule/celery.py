from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab
from django.conf import settings
from django.utils import timezone
from pathlib import Path
from kombu import Queue
from datetime import timedelta
from typing import Any

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    ELASTIC_SSL=(bool, False),
    STRESS_TEST=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

environ.Env.read_env(BASE_DIR / ".env")

# schedule 為專案名稱
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"django_base.settings.{env('DEV')}")

# 使用redis作為中間人(broker)
# 使用redis作為定時任務存取地方(backend)
# 預設redis為本地127.0.0.1:6379/1(redis)
# ★★★ 此處須注意(若本地沒有redis卻設置redis預設 -> 則會顯示10061連線錯誤)
app = Celery("schedule")


# 從單獨的配置模組中載入配置
# app.config_from_object("django.conf:settings", namespace="CELERY")
app.config_from_object("schedule.celeryConfig", namespace="CELERY")

# 設定app自動載入任務
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# 允許root用戶運行celery
platforms.C_FORCE_ROOT = True

# 有出錯會顯示於此
@app.task(bind=True)
def debug_task(self: Any) -> None:
    print("Request: {0!r}".format(self.request))


# 設定任務進入哪個列隊 (在開啟worker時，可以分別進行)
app.conf.task_routes = {
    "autoGenLogPartitionTable": {"queue": "tasks_one"},
}

# 設定列隊路由
app.conf.task_queues = (
    Queue("tasks_one", routing_key="tasks_one"),
)

# 固定的定時任務
app.conf.update(
    CELERY_BEAT_SCHEDULE={
        "autoGenLogPartitionTable": {
            "task": "autoGenLogPartitionTable",
            "schedule": timedelta(weeks=8),
            "args": ([],),
        },
    }
)
