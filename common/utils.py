from datetime import datetime

from django.utils import timezone


def parse_date(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            pass
    return timezone.localdate()
