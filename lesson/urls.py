from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import LessonApiList, LessonApiCreate, LessonApiUpdate, LessonApiRetrieve, LessonApiDelete

app_name = LessonConfig.name

urlpatterns = [
    path('lesson/', LessonApiList.as_view(), name='lesson_list'),
    path('lesson/create/', LessonApiCreate.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonApiUpdate.as_view(), name='lesson_update'),
    path('lesson/detail/<int:pk>/', LessonApiRetrieve.as_view(), name='lesson_detail'),
    path('lesson/destroy/<int:pk>/', LessonApiDelete.as_view(), name='lesson_destroy'),

]
