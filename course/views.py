from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response, viewsets
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import OrderingFilter
from course.models import Course, Payments
from course.serializer import CourseSerializer, PaymentsSerializer, CourseCreateSerializer
from lesson.permissions import StaffPermission, ObjPermission


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        'create': CourseCreateSerializer,
    }
    permission_classes = [StaffPermission, ObjPermission]

    def get_queryset(self):
        queryset = Course.objects.all()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        if self.request.user.is_active:
            return queryset.filter(id__in=[i.id for i in self.request.user.course.all()])


    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_method')
    ordering_field = ('payment_date',)
    permission_classes = [StaffPermission, ObjPermission]
