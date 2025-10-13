from datetime import timedelta

import logging
from celery import shared_task
from django.db.models import Q
from django.utils import timezone

from users.models import User
logger = logging.getLogger(__name__)

@shared_task
def disable_inactive_users():
    termination_date = timezone.now() - timedelta(days=30)

    inactive_users = User.objects.filter(
        is_active=True
    ).filter(
        Q(last_login__lt=termination_date) |
        Q(last_login__isnull=True, date_joined__lt=termination_date)
    )

    count = inactive_users.count()
    inactive_users.update(is_active=False)

    logger.info(f"Disabled {count} inactive users")
