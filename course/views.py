import os

import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.filters import OrderingFilter

from config.services import set_check
from config.tasks import user_activity
from course.models import Course, Payments, Subscription
from course.permissions import StaffPermissionViewSet, SubscriptionPermission
from course.serializer import CourseSerializer, CourseCreateSerializer, PaymentsSerializer, SubscriptionSerializer, \
    SubscriptionCreateSerializer, PaymentCreateSerializer, PaymentDetailSerializer

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
    default_serializer = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_method')
    ordering_field = ('payment_date',)
    permission_classes = [StaffPermissionViewSet, ObjPermission]
    serializers = {
        'create': PaymentCreateSerializer,
        "retrieve": PaymentDetailSerializer
    }

    def get_object(self):
        stripe.api_key = os.getenv("API_KEY")
        obj = super().get_object()
        obj = Payments.objects.get(pk=self.kwargs.get("pk"))

        retrieve_session = stripe.checkout.Session.retrieve(
            obj.url_session,
        )
        if retrieve_session['payment_status'] == "paid":
            obj.paid = True
        obj.save()
        return obj

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


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
