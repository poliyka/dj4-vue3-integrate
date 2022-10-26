import os
from getpass import getpass

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

FIXTURE_DIR = settings.BASE_DIR / "fixtures"


class Command(BaseCommand):
    help = "Initialize procedures"

    REG_CREATE_SUPERUSER = "init.create_superuser"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--force", action="store_true", help="force import")

    def handle(self, *args, **options):
        if options["force"]:
            self.stdout.write("Clear registry...")

            # clear build
            self.stdout.write("Clear build...")

        self.stdout.write("Creating superuser...")
        self.create_superuser()
        # Try to create superuser
        # Skip if it has a registry that says it is already done
        # if self.REG_CREATE_SUPERUSER not in reg:
        #     self.stdout.write("Creating superuser...")
        #     self.create_superuser()
        #     reg[self.REG_CREATE_SUPERUSER] = True


    def create_superuser(self):
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

        user = User.objects.create_superuser(username, email, password)
        # profile = Profile(user=user)
        # profile.save()
