from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from django.utils.timezone import now
from django.contrib.auth import get_user_model
@shared_task
def send_course_update_email(user_email, course_title, message):
    send_mail(
        subject=f"Обновление курса: {course_title}",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
    )




@shared_task
def deactivate_inactive_users():
    User = get_user_model()
    one_month_ago = now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    inactive_users.update(is_active=False)
