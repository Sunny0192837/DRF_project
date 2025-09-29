from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="aboba@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            title="Some course", description="Some info", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="Какой-то урок о чем-то",
            description="Какое-то содержание какого-то урока",
            owner=self.user,
        )

    def test_lesson_retrieve(self):
        url = reverse_lazy("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data,
            {
                "id": self.lesson.pk,
                "video_link": None,
                "title": "Какой-то урок о чем-то",
                "preview": None,
                "description": "Какое-то содержание какого-то урока",
                "course": self.course.pk,
                "owner": self.user.pk,
            },
        )

    def test_lesson_create(self):
        url = reverse_lazy("materials:lesson_create")
        data = {
            "title": "пример урока",
            "description": "пример описания урока",
            "video_link": "https://www.youtube.com/aboba",
        }
        response = self.client.post(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(
            result,
            {
                "id": 2,
                "video_link": "https://www.youtube.com/aboba",
                "title": "пример урока",
                "preview": None,
                "description": "пример описания урока",
                "course": None,
                "owner": 1,
            },
        )

    def test_lesson_update(self):
        url = reverse_lazy("materials:lesson_update", args=(self.lesson.pk,))
        data = {"title": "Измененный урок"}
        response = self.client.patch(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Измененный урок", data.get("title"))

    def test_lesson_delete(self):
        url = reverse_lazy("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse_lazy("materials:lesson_list")
        response = self.client.get(url)
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_link": None,
                    "title": self.lesson.title,
                    "preview": None,
                    "description": self.lesson.description,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

