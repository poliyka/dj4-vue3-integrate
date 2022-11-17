from __future__ import absolute_import

from celery import shared_task
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from django.core.management import call_command
from typing import Any


@shared_task(name="autoGenLogPartitionTable", bind=True)
def genPartitionTable(self: Any, *args: Any, **kwargs: Any) -> Any:
    call_command("pgpartition", "-y")
