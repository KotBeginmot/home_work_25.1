from rest_framework import serializers

from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
