from django.contrib.auth.models import AbstractUser
from django.db import models


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
