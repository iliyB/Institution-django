import datetime

from django.utils import timezone


def get_current_time() -> datetime.datetime:
    return timezone.localtime(timezone.now())
