from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Create courses, lessons and payments"

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        user1 = User.objects.get_or_create(email="123@example.com")[0]
        user1.set_password("123qweasdzxc")
        user1.is_active = True

        course1 = Course.objects.create(
            title="Первый курс",
            description="Какое-то описание какого-то курса о чем-то",
        )
        lesson1 = Lesson.objects.create(
            course=course1,
            title="Какой-то урок о чем-то",
            description="Какое-то содержание какого-то урока",
        )
        lesson2 = Lesson.objects.create(
            course=course1,
            title="Второй урок о чем-то",
            description="Какое-то содержание второго урока",
        )
        lesson3 = Lesson.objects.create(
            course=course1,
            title="Третий урок о чем-то",
            description="Какое-то содержание третьего урока",
        )

        course2 = Course.objects.create(
            title="Второй курс",
            description="Какое-то описание какого-то курса о чем-то",
        )
        lesson4 = Lesson.objects.create(
            course=course2,
            title="Какой-то урок о чем-то",
            description="Какое-то содержание какого-то урока",
        )
        lesson5 = Lesson.objects.create(
            course=course2,
            title="Второй урок о чем-то",
            description="Какое-то содержание второго урока",
        )
        lesson6 = Lesson.objects.create(
            course=course2,
            title="Третий урок о чем-то",
            description="Какое-то содержание третьего урока",
        )
        payment1 = Payment.objects.create(
            user=user1,
            paid_course=course1,
            date='2024-04-04',
            amount=30000,
            method="transfer",
        )
        payment2 = Payment.objects.create(
            user=user1,
            paid_course=course2,
            date='2023-03-03',
            amount=30000,
            method="cash",
        )
        payment3 = Payment.objects.create(
            user=user1,
            paid_lesson=lesson1,
            date='2025-05-05',
            amount=3000,
            method="cash",
        )
        payment4 = Payment.objects.create(
            user=user1,
            paid_lesson=lesson6,
            date='2022-02-02',
            amount=3000,
            method="transfer",
        )
