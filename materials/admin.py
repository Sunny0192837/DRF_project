from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
    )
    list_filter = ("title",)
    search_fields = ("description",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "course",
        "description",
    )
    list_filter = ("title", "course")
    search_fields = ("description", "course")
