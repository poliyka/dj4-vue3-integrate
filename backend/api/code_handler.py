from enum import Enum

from django.utils.translation import gettext_lazy as _

# BS0000 ~ BS9999: success
# BE1000 ~ BE1999: common error
# BE2000 ~ BE2999: auth error
# BE3000 ~ BE3999: user error
# BE4000 ~ BE4999: project error
# BE5000 ~ BE5999: task error
# BE6000 ~ BE6999: comment error
# BE7000 ~ BE7999: file error
# BE8000 ~ BE8999: notification error
# BE9000 ~ BE9999: other error
# BE10000 ~ BE10999: system error
# BE11000 ~ BE11999: test error
# BE12000 ~ BE12999: go api error


class Code(Enum):
    # BS0000 ~ BS9999: success
    SUCCESS = "BS200"
    SUCCESS_NO_RESPONSE = "BS201"

    # BE1000 ~ BE1999: common error
    # BE2000 ~ BE2999: auth error
    HTTP403_FORBIDDEN = "BE2000"
    JWT_TOKEN_EXPIRE = "BE2001"
    USERNAME_OR_PASSWORD_NOT_FOUND = "BE2002"
    # BE3000 ~ BE3999: user error
    USER_NETWORK_IN_CORRECT = "BE3000"

    # BE4000 ~ BE4999: project error
    JOB_ID_NOT_EXISTS = "BE4000"
    PROJECT_NAME_EXISTS = "BE4001"
    JOB_DELETE_HAVE_UP_DOWN_STREAM = "BE4002"
    USER_IS_EXISTS = "BE4003"
    USER_EMAIL_IS_EXISTS = "BE4004"
    FORM_DATA_IS_NOT_VALID = "BE4005"
    UP_DOWN_STREAM_HAVE_SAME_ID = "BE4006"
    INVALID_CRONTAB_EXPRESSION = "BE4007"
    PROJECT_NOT_FOUND = "BE4008"

    # BE6000 ~ BE6999: comment error
    # BE7000 ~ BE7999: file error
    # BE8000 ~ BE8999: notification error
    # BE9000 ~ BE9999: other error
    # BE10000 ~ BE10999: system error
    HTTP400_BAD_REQUEST = "BE10000"
    HTTP_404_NOT_FOUND = "BE10001"
    HTTP_500_INTERNAL_SERVER_ERROR = "BE10002"
    SYSTEM_NETWORK_ERROR = "BE10003"
    HTTP_401_UNAUTHORIZED = "BE10004"
    # BE11000 ~ BE11999: test error

    # BE12000 ~ BE12999: go api error
    GO_SERVICE_ERROR = "BE12000"
    GO_DATA_EXEC_DTTM_NOT_EXISTS = "BE12001"
    GO_JOB_ID_NOT_EXISTS = "BE12002"
    GO_SCHE_DTTM_GT_NEXT = "BE12003"
    GO_JOB_FAIL = "BE12004"
    GO_JOB_DUPLICATE = "BE12005"
    GO_QUE_ERROR = "BE12006"
    GO_EXP_ERROR = "BE12007"
    GO_EXP_VER_ERROR = "BE12008"
    GO_EXP_UPDATE_ERROR = "BE12009"
    GO_IMP_SCHE_CODE_ERROR = "BE12010"
    GO_IMP_STATUS_CODE_ERROR = "BE12011"
    GO_IMP_ERROR = "BE12012"


class CodeMsg(Enum):
    # BS0000 ~ BS9999: success
    BS200 = _("[BS200] Success")
    BS201 = _("[BS201] Success without Response")

    # BE1000 ~ BE1999: common error
    # BE2000 ~ BE2999: auth error
    BE2000 = _("[BE2000] Insufficient authority")
    BE2001 = _("[BE2001] Login timeout, please log in again")
    BE2002 = _("[BE2002] Account or password error")
    # BE3000 ~ BE3999: user error
    BE3000 = _(
        "[BE3000]: There is something wrong with the network, please check the connection status and reset the page"
    )

    # BE4000 ~ BE4999: project error
    BE4000 = _("[BE4000] Job is not exists")
    BE4001 = _("[BE4001] Project Name already exists")
    BE4002 = _(
        "[BE4002] Following jobs exists Upstream or Downstream, please cancel its relationship before deleting:{job_names}"
    )
    BE4003 = _("[BE4003] Account already exists")
    BE4004 = _("[BE4004] '{email}' This email already exists")
    BE4005 = _("[BE4005] Form data have some errors, please check and submit again")
    BE4006 = _("[BE4006] Upstream and Downstream can't have same job")
    BE4007 = _("[BE4007] Invalid Crontab Expression")
    BE4008 = _("[BE4008] Project not found")

    # BE6000 ~ BE6999: comment error
    # BE7000 ~ BE7999: file error
    # BE8000 ~ BE8999: notification error
    # BE9000 ~ BE9999: other error
    # BE10000 ~ BE10999: system error
    BE10000 = _("[BE10000] Bad request")
    BE10001 = _("[BE10001] Could not find the relevant page")
    BE10002 = _("[BE10002] Internal server error")
    BE10003 = _("[BE10003] There is a problem with the server network, please try again later")
    BE10004 = _("[BE10004] Please log in first")
    # BE11000 ~ BE11999: test error

    # BE12000 ~ BE12999: go api error
    BE12000 = _(
        "[BE12000] There is a problem with the server network, please try again later or contact the administrator"
    )
    BE12001 = _("[BE12001] Data execution time (job_exec_dttm) does not exist")
    BE12002 = _("[BE12002] Job ID does not exist")
    BE12003 = _("[BE12003] Schedule time is greater than next execution time")
    BE12004 = _("[BE12004] Job execution failed")
    BE12005 = _("[BE12005] Job is already running")
    BE12006 = _("[BE12006] Queue processing failed")
    BE12007 = _("[BE12007] Export data error")
    BE12008 = _("[BE12008] Export version does not exist")
    BE12009 = _("[BE12009] Export update failed")
    BE12010 = _("[BE12010] Import schedule data checksum error")
    BE12011 = _("[BE12011] Import code data checksum error")
    BE12012 = _("[BE12012] Import job failed")


def getCodeMsg(code: Code, fmt: dict = {}) -> str:
    # 從前端取得語系
    return CodeMsg[code.value].value.format(**fmt)
