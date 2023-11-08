import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def set_check():

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='user_activity',
        task='config.tasks.user_activity',
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
