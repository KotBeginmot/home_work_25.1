from rest_framework import serializers

from course.models import Payments
from course.serializer import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payment_date = serializers.SerializerMethodField()

    def get_payment_date(self, i):
        return [i.payment_date for i in i.users_pay.all()]

    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'user_phone', 'user_city')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'user_phone', 'user_city', 'avatar', 'course', 'lesson')


class SelfUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
