from rolepermissions.roles import AbstractUserRole

# https://django-role-permissions.readthedocs.io/en/stable/quickstart.html


# Role permissions:
# - Admin : All permission
# - Maintainer: All permission exclude assign Maintainer permission
# - Developer: Can CRUD
# - Viewer: Only view

# Saas permissions:
# - Standard
# - Gold
# - Platinum
# - Enterprise


class Operator(AbstractUserRole):
    available_permissions = {
        # 最高權限
        "Admin": False,
        # 管理者
        "Maintainer": False,
        # 操作者
        "Developer": False,
        # read only
        "Viewer": True,
    }


class Saas(AbstractUserRole):
    available_permissions = {
        "Standard": True,
        "Gold": False,
        "Platinum": False,
        "Enterprise": False,
    }
