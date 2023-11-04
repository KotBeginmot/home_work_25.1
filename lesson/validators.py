from rest_framework import serializers


class LessonValidation:
    def __call__(self, value):
        yt = "www.youtube.com"
        if value:
            if yt != value[value.find('://') + 3:].split('/')[0] or len(value.split()) > 2 or len(
                    value[value.find('://') + 3:].split('/')) > 2:
                raise serializers.ValidationError('Нельзя сохранять ссылки на стороние объекты , только ю-туб')
        else:
            raise serializers.ValidationError('Введите ссылку')
