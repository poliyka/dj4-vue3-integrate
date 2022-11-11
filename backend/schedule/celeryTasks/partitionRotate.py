from __future__ import absolute_import

from celery import shared_task
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from django.core.management import call_command

import datetime as dt

run_date = (dt.date.today()).strftime('%Y-%m-%d')

@shared_task(name='autoGenLogPartitionTable', bind=True)
def genPartitionTable(self, *args, **kwargs):
    call_command('createschema')
    return "OnCalled"

@shared_task(name='testTask', bind=True, max_retries=5, default_retry_delay=10)
def testTask(self, *args, **kwargs):
    aa = 1/0
    return "Ontest"

