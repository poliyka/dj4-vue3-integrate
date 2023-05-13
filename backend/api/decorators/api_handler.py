import logging
import traceback
from functools import wraps

from api.code_handler import Code
from api.utils.common import resMsg, LogRecord
from log.models import Log

logger = logging.getLogger(__name__)


class ErrorHandler:
    def __init__(self, title: str, action, err_level, err_code=None, data=None, handle_info=True):
        self.title = title or "Something"
        self.action = action
        self.err_level = err_level
        self.err_code = err_code or Code.HTTP_500_INTERNAL_SERVER_ERROR
        self.data = data
        self.handle_info = handle_info

    def __call__(self, func):
        @wraps(func)
        def callable(obj, *args, **kwargs):
            try:
                log_record = LogRecord(
                    method=obj.__class__.__name__ + "/" + obj.request.method,
                    action=self.action,
                    level=Log.Level.INFO,
                    user=obj.request.user,
                    api=obj.request.path,
                    info=f"{self.title}",
                    message="",
                    data=self.data,
                )
                res_msg = func(log_record, *args, **kwargs)

                if self.handle_info:
                    log_record.save()

                return res_msg
            except:
                logger.error("%s failed: %s", self.title, traceback.format_exc())
                log_record = LogRecord(
                    method=obj.__class__.__name__ + "/" + obj.request.method,
                    action=self.action,
                    level=self.err_level,
                    user=obj.request.user,
                    api=obj.request.path,
                    info=f"{self.title} failed",
                    message=traceback.format_exc(),
                    data=self.data,
                )

                return resMsg(self.err_code, data=obj.request.data, fail=True)

        return callable
