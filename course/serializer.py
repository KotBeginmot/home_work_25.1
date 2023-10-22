from rest_framework import serializers

from course.models import Course, Payments
from lesson.models import Lesson
from lesson.serializer import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set', many=True)
    lessons_count = serializers.SerializerMethodField()
    def get_lessons_count(self, instance):
        return instance.lesson_set.all().count()


    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'preview', 'description')

    def create(self, validated_data):
        self.course = Course.objects.create(**validated_data)

        return self.course


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
