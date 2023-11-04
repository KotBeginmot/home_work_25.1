from rest_framework import serializers

from course.models import Course, Payments, Subscription
from course.services import user_check, stripe_work
from lesson.serializer import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_lessons_count(self, instance):
        return instance.lesson_set.all().count()

    def get_subscription(self, instance):
        return user_check(self, instance)

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


class PaymentCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Payments.objects.create(**validated_data)
        stripe_response = stripe_work(self, validated_data)
        obj.url = stripe_response[0].get('url')
        obj.url_session = stripe_response[2]
        if stripe_response[1]['payment_status'] != "unpaid":
            obj.paid = True
        else:
            obj.paid = False
        obj.save()
        return obj

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email', read_only=True)
    course = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if self.data['course'] in [i.course.id for i in Subscription.objects.all().filter(user=validated_data['user'])]:
            raise serializers.ValidationError('Можно создать только одну подписку между пользователем и курсом')
        self.subscription = Subscription.objects.create(**validated_data)
        return self.subscription

    class Meta:
        model = Subscription
        fields = '__all__'
