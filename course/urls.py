from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, PaymentsViewSet, SubscriptionAPIViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet, basename='payments')
router.register(r'subscription', SubscriptionAPIViewSet, basename='subscription')


urlpatterns = [] + router.urls
