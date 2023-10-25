from rest_framework import serializers

from users.models import User


def user_create(request):
    try:
        request.data['password']
    except Exception:
        raise serializers.ValidationError('Пароль обязателен')

    data_email = request.data['email']
    if not data_email or len(set(['@', '.']).intersection(set(data_email))) < 2 or \
            data_email in [i.email for i in User.objects.all()] or data_email.count('@') > 1:
        raise serializers.ValidationError('Неправильный е-меил , или уже существующий')
    if not request.data['password'] or len(request.data['password']) < 5:
        raise serializers.ValidationError('Неправильный пароль')
