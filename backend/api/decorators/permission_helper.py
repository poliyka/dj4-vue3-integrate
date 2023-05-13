from functools import wraps

# from base.roles import Operator, Saas
from rolepermissions.permissions import available_perm_status
from django.contrib.auth.models import User
from rest_framework.response import Response
from api.code_handler import Code
from api.utils.common import resMsg
from rest_framework.status import HTTP_403_FORBIDDEN
from base.roles import Operator

# Reference:
# https://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html
# https://django-role-permissions.readthedocs.io/en/stable/


class PermissionBase:
    def has_permissions(self, user: User, allows: list = []):
        """
        permission like this:
        {
            'Admin': False,
            'Maintainer': False,
            'Developer': True,
            'Viewer': True,
            'Standard': True,
            'Gold': False,
            'Platinum': False,
            'Enterprise': False
        }
        """
        permissions = available_perm_status(user)
        for allow in allows:
            if permissions.get(allow):
                return True
        return False

    def any_permissions(self, user: User):
        op_perms = list(Operator.available_permissions.keys())
        permissions = available_perm_status(user)
        for perm in op_perms:
            if permissions.get(perm):
                return True
        return False


class PermissionAllow(PermissionBase):
    def __init__(self, allows: list = []):
        self.allows = allows

    def __call__(self, func):
        @wraps(func)
        def callable(request, *args, **kwargs):
            # 從前端取得登入使用者
            user = request.user

            # 如果使用者是 anonymous 回傳無權限
            # 此為保險起見，因為前端應該會先檢查是否登入
            if user.is_anonymous:
                return Response(resMsg(Code.HTTP403_FORBIDDEN, fail=True), status=HTTP_403_FORBIDDEN)

            # 如果 allows 含有 __all__ 且具有任一 Operator 權限直接通過
            if "__all__" in self.allows and self.any_permissions(user):
                return func(request, *args, **kwargs)

            # 檢查使用者是否有權限
            if not self.has_permissions(user, self.allows):
                return Response(resMsg(Code.HTTP403_FORBIDDEN, fail=True), status=HTTP_403_FORBIDDEN)

            return func(request, *args, **kwargs)

        return callable
