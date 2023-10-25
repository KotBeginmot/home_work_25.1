from django.db import models

from course.models import NULLABLE


class Lesson(models.Model):
    objects = None
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                               )
    name = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_link = models.URLField(max_length=50, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

