from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Create courses, lessons and payments"

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        moder = User.objects.get_or_create(email="moderator@example.com")[0]
        moder.set_password("123qweasdzxc")
        moder.is_active = True
        moder.groups.add(1)
        moder.save()

        not_moder = User.objects.get_or_create(email="NEmoderator@example.com")[0]
        not_moder.set_password("123qweasdzxc")
        not_moder.is_active = True
        not_moder.save()

        not_owner = User.objects.get_or_create(email="NEowner@example.com")[0]
        not_owner.set_password("123qweasdzxc")
        not_owner.is_active = True
        not_owner.save()


        course1 = Course.objects.create(
            title="Первый курс",
            description="Какое-то описание какого-то курса о чем-то",
            owner=not_moder
        )
        lesson1 = Lesson.objects.create(
            course=course1,
            title="Какой-то урок о чем-то",
            description="Какое-то содержание какого-то урока",
            owner=not_moder
        )
        lesson2 = Lesson.objects.create(
            course=course1,
            title="Второй урок о чем-то",
            description="Какое-то содержание второго урока",
            owner=not_moder
        )
        lesson3 = Lesson.objects.create(
            course=course1,
            title="Третий урок о чем-то",
            description="Какое-то содержание третьего урока",
            owner=not_moder
        )

        course2 = Course.objects.create(
            title="Второй курс",
            description="Какое-то описание какого-то курса о чем-то",
            owner=not_moder
        )
        lesson4 = Lesson.objects.create(
            course=course2,
            title="Какой-то урок о чем-то",
            description="Какое-то содержание какого-то урока",
            owner=not_moder
        )
        lesson5 = Lesson.objects.create(
            course=course2,
            title="Второй урок о чем-то",
            description="Какое-то содержание второго урока",
            owner=not_moder
        )
        lesson6 = Lesson.objects.create(
            course=course2,
            title="Третий урок о чем-то",
            description="Какое-то содержание третьего урока",
            owner=not_moder
        )
        payment1 = Payment.objects.create(
            user=not_moder,
            paid_course=course1,
            date="2024-04-04",
            amount=30000,
            method="transfer",
        )
        payment2 = Payment.objects.create(
            user=not_moder,
            paid_course=course2,
            date="2023-03-03",
            amount=30000,
            method="cash",
        )
        payment3 = Payment.objects.create(
            user=not_moder,
            paid_lesson=lesson1,
            date="2025-05-05",
            amount=3000,
            method="cash",
        )
        payment4 = Payment.objects.create(
            user=not_moder,
            paid_lesson=lesson6,
            date="2022-02-02",
            amount=3000,
            method="transfer",
        )
