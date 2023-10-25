from rest_framework import serializers

from lesson.models import Lesson
from lesson.validators import LessonValidation


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name', read_only=True)
    video_link = serializers.URLField(validators=[LessonValidation()])
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[LessonValidation()])
    class Meta:
        model = Lesson
        fields = '__all__'