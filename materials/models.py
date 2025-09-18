from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Укажите название курсе"
    )
    preview = models.ImageField(
        upload_to="materials/courses/previews",
        blank=True,
        null=True,
        verbose_name="Превью курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Курс",
        help_text="Выберите курс",
        related_name="lessons",
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Название уровка",
        help_text="Укажите название урока",
    )
    preview = models.ImageField(
        upload_to="materials/lessons/previews",
        blank=True,
        null=True,
        verbose_name="Превью урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )
    video_link = models.URLField(
        verbose_name="Сслыка на видео",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name = "Уроки"
