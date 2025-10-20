from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User

@shared_task
def send_course_update_mail(course_id, title):
    recipients = User.objects.filter(subscription__course_id=course_id)
    emails = []

    for user in recipients:
        emails.append(user.email)
    send_mail(
        'Course update!',
        f'Course {title}, you are subscribed to, got an update!',
        from_email=EMAIL_HOST_USER,
        recipient_list=emails
    )
