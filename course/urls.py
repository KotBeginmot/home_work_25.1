from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, PaymentsViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('payments', PaymentsViewSet, basename='payments')


urlpatterns = [] + router.urls
