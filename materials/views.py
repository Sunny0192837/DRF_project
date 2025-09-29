from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from materials.paginators import LessonPaginator, CoursePaginator
from materials.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    LessonSerializer,
)
from users.models import Subscription
from users.permissions import IsModerator, IsOwner


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def get_queryset(self):
        queryset = Course.objects.all()
        if not self.request.user.groups.filter(name="Moderators").exists():
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~IsModerator]
        elif self.action in ["update", "partial_update", "retrieve"]:
            self.permission_classes = [
                IsModerator | IsOwner,
            ]
        elif self.action == "destroy":
            self.permission_classes = [~IsModerator & IsOwner]
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LessonPaginator

    def get_queryset(self):
        queryset = Lesson.objects.all()
        if not self.request.user.groups.filter(name="Moderators").exists():
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [~IsModerator & IsOwner]


class SubscriptionSwitchView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("id")
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(course=course_item, user=user)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(course=course_item, user=user)
            message = "Подписка добавлена"

        return Response({"course_id": course_id, "message": message})
