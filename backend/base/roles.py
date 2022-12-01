from rolepermissions.roles import AbstractUserRole

# https://django-role-permissions.readthedocs.io/en/stable/quickstart.html

class Group1(AbstractUserRole):
    available_permissions = {
        'permission1': True,
        'permission2': True,
    }

class Group2(AbstractUserRole):
    available_permissions = {
        'permission1': True,
        'permission2': True,
        'permission3': True,
    }
