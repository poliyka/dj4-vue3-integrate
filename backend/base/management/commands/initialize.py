import os

# Typing
from argparse import ArgumentParser
from getpass import getpass
from typing import Any

from base.models import Profile
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from registry.helper import reg

# from registry.models import Entry
from rolepermissions.permissions import grant_permission
from rolepermissions.roles import assign_role
from base.roles import Operator, Saas

FIXTURE_DIR = settings.BASE_DIR / "fixtures"


class Command(BaseCommand):
    help = "Initialize procedures"

    REG_CREATE_SUPERUSER = "init.create_superuser"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("-f", "--force", action="store_true", help="force import")

        parser.add_argument("-d", "--demo", action="store_true", help="demo data")

    def handle(self, *args: Any, **options: Any) -> None:
        if options["force"]:
            self.stdout.write("Clear registry...")

            # clear build
            self.stdout.write("Clear build...")

        # Try to create superuser
        # Skip if it has a registry that says it is already done
        if self.REG_CREATE_SUPERUSER not in reg:
            self.stdout.write("Creating superuser...")
            self.create_superuser()
            reg[self.REG_CREATE_SUPERUSER] = True

        if options["demo"]:
            self.stdout.write("Creating demo data...")
            self.demo()

    def create_superuser(self) -> None:
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME") or input("Please enter username: ")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL") or input("Please enter email: ")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD") or getpass("Please enter password: ")

        if not username:
            self.stdout.write("No given username, abort creating superuser...")
            return

        User = get_user_model()
        if username:
            if User.objects.filter(username=username).exists():
                self.stdout.write("User already exists")
                return

        # admin
        admin = User.objects.create_superuser(username, email, password)
        profile = Profile(user=admin)
        profile.save()

        # assign role group
        assign_role(admin, Operator)
        assign_role(admin, Saas)
        # grant admin permissions
        grant_permission(admin, "Admin")

    def demo(self) -> None:
        User = get_user_model()
        roles = ["Admin", "Maintainer", "Developer", "Viewer", "Standard", "Gold", "Platinum", "Enterprise"]

        for r in roles:
            user = User.objects.create_user(r, f"{r}@example.com", "root")
            user.first_name = r
            user.save()
            profile = Profile(user=user)
            profile.save()

            # assign role group
            assign_role(user, Operator)
            assign_role(user, Saas)
            # grant admin permissions
            grant_permission(user, r)
