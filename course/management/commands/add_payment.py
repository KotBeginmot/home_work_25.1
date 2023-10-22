from django.core.management import BaseCommand

from course.models import Payments


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = Payments.objects
        payment.create(
            course_id=1,
            lesson_id=1,
            user_id=1,
            paid=True,
            payment_method='card'

        )
