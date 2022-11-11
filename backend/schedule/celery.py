from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab
from datetime import timedelta
from kombu import Queue  # 用於多任務列隊

# django_DRF 為專案名稱
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule.settings")

# 使用redis作為中間人(broker)
# 使用redis作為定時任務存取地方(backend)
# 預設redis為本地127.0.0.1:6379/1(redis)
# ★★★ 此處須注意(若本地沒有redis卻設置redis預設 -> 則會顯示10061連線錯誤)
app = Celery("Django_DRF", backend="redis://127.0.0.1:6379/14", broker="redis://127.0.0.1:6379/15")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# 預設任務名稱為tasks用意為此，此行會加載已經有註冊的app.task.py檔案
app.autodiscover_tasks()
# 設定任務進入哪個列隊 (在開啟worker時，可以分別進行)
app.conf.task_routes = {
    "AppName1.tasks.TF_postingJob": {"queue": "tasks_one"},
    "AppName2.tasks.MLO_dailyDataJob": {"queue": "tasks_two"},
}
# 設定列隊路由
app.conf.task_queues = (
    Queue("tasks_one", routing_key="tasks_one"),
    Queue("tasks_two", routing_key="tasks_two"),
)
# 允許root用戶運行celery
platforms.C_FORCE_ROOT = True
# 有出錯會顯示於此
@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


# 固定的定時任務
app.conf.update(
    CELERYBEAT_SCHEDULE={
        "JobName": {  # 任務名稱
            "task": "app.tasks.functionName",  # 執行的任務
            "schedule": timedelta(seconds=5),  # 週期多久一次
            "args": (),  # 此處可帶參數
        }
    }
)
