from rest_framework import generics
from django.shortcuts import render

from lesson.models import Lesson
from lesson.permissions import StaffPermission, ObjPermission
from lesson.serializer import LessonSerializer


class LessonApiList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Lesson.objects.all()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        if self.request.user.is_active:
            return queryset.filter(id__in=[i.id for i in self.request.user.lesson.all()])

    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [StaffPermission]


class LessonApiCreate(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [StaffPermission]


class LessonApiUpdate(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [StaffPermission, ObjPermission]


class LessonApiRetrieve(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [StaffPermission, ObjPermission]


class LessonApiDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [StaffPermission, ObjPermission]
