from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import OrderingFilter
from course.models import Course, Payments, Subscription
from course.permissions import StaffPermissionViewSet, SubscriptionPermission
from course.serializer import CourseSerializer, CourseCreateSerializer, PaymentsSerializer, SubscriptionSerializer, \
    SubscriptionCreateSerializer
from lesson.paginations import MyPagination

from lesson.permissions import ObjPermission


class CourseViewSet(ModelViewSet):
    # queryset = Course.objects.all()
    default_serializer = CourseSerializer
    pagination_class = MyPagination
    serializers = {
        'create': CourseCreateSerializer,
    }
    permission_classes = [StaffPermissionViewSet, ObjPermission]

    def get_queryset(self):
        queryset = Course.objects.all()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        if self.request.user.is_active:
            return queryset.filter(id__in=[i.id for i in self.request.user.course.all()])
        return queryset

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_method')
    ordering_field = ('payment_date',)
    permission_classes = [StaffPermissionViewSet, ObjPermission]


class SubscriptionAPIViewSet(ModelViewSet):
    pagination_class = MyPagination
    queryset = Subscription.objects.all()
    default_serializer = SubscriptionSerializer
    serializers = {
        'create': SubscriptionCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    permission_classes = [SubscriptionPermission]
