from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Укажите почту", max_length=50
    )
    phone_number = models.CharField(
        max_length=35, blank=True, null=True, verbose_name="номер телефона"
    )
    city = models.CharField(max_length=35, blank=True, null=True, verbose_name="город")
    profile_image = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="фото профиля"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ("Пользователь",)
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    payment_methods = [("transfer", "Перевод на счет"), ("cash", "Наличными")]
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Пользователь"
    )
    date = models.DateField(
        verbose_name="Дата оплаты",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Купленный урок',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    paid_course = models.ForeignKey(
        Course,
        verbose_name='Купленный курс',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты",
    )
    method = models.CharField(choices=payment_methods)
