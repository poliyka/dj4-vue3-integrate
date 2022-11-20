from django.conf import settings

# Celery settings
# 指定 Backend
CELERY_RESULT_BACKEND = "django-db"
# CELERY_RESULT_BACKEND = f"{settings.REDIS_URL}/15"

# 指定時區，預設是 UTC
CELERY_TIMEZONE = settings.TIME_ZONE
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False

# celery 序列化與反序列化配置
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_IGNORE_RESULT = True
# celery 的啟動工作數量設定
CELERY_WORKER_CONCURRENCY = 10
# 任務預取功能，會盡量多拿 n 個，以保證獲取的通訊成本可以壓縮。
CELERYD_PREFETCH_MULTIPLIER = 20
# 有些情況下可以防止死鎖
CELERYD_FORCE_EXECV = True
# celery 的 worker 執行多少個任務後進行重啟操作
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
# 禁用所有速度限制，如果網路資源有限，不建議開足馬力。
CELERY_DISABLE_RATE_LIMITS = True
# celery worker log format
CELERY_WORKER_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(processName)s: %(message)s"
# 此設定會影響 task result 的紀錄
CELERY_RESULT_EXTENDED = True

# celery beat配置（週期性任務設定）
CELERY_BROKER_URL = f"{settings.REDIS_URL}/14"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
