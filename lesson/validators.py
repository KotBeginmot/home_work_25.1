from rest_framework import serializers


class LessonValidation:
    def __call__(self, value):
        yt = "www.youtube.com"
        if value:
            if yt != value[value.find('://') + 3:].split('/')[0] or len(value.split()) > 2 or len(
                    value[value.find('://') + 3:].split('/')) > 2:
                raise serializers.ValidationError('Можно добавить ссылки  только на youtube')
        else:
            raise serializers.ValidationError('Введите ссылку')
