import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Course
from users.models import User


@shared_task
def check_update(obj_course_id, lesson_name):
    obj_course = Course.objects.get(pk=obj_course_id)
    subscriptions = obj_course.subscription_set.filter(subscription=True)
    send_mail(
        subject="Обновление курса",
        message=f"Урок {lesson_name} курса {obj_course.name} обновлен",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[i.user.email for i in subscriptions.all()]
    )


def user_activity():
    days_to_deactivate = 30
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if (datetime.datetime.now() - user.last_login.replace(tzinfo=None)).days > days_to_deactivate:
                user.is_active = False
                user.save()
