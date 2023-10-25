from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import AllowAny

from lesson.models import Lesson
from lesson.paginations import MyPagination
from lesson.permissions import StaffPermission, ObjPermission
from lesson.serializer import LessonSerializer, LessonCreateSerializer


class LessonApiList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [StaffPermission]
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Lesson.objects.all()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        if self.request.user.is_active:
            return queryset.filter(id__in=[i.id for i in self.request.user.lesson.all()])


class LessonApiCreate(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    permission_classes = [StaffPermission, AllowAny]


class LessonApiUpdate(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [StaffPermission, ObjPermission]


class LessonApiRetrieve(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [StaffPermission, ObjPermission]


class LessonApiDelete(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [StaffPermission, ObjPermission]
