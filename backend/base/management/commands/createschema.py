from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from typing import Any

from django.db import connection


class Command(BaseCommand):
    help = "Create db schema"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("-f", "--force", action="store_true", help="force import")

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Create db schema...")
        self.create_schema()

    def create_schema(self) -> None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("CREATE SCHEMA django;")
            except Exception as err:
                self.stdout.write(str(err))

