from rest_framework import serializers


def user_check(obj, instance):
    user = obj.context['request'].user
    return (instance.subscription_set.get(user=user).subscription if user in [i.user for i in
                                                                                    instance.subscription_set.all()] else 'не студент курса')
