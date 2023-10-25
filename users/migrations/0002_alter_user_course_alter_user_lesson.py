# Generated by Django 4.2.6 on 2023-10-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        ('course', '0003_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(blank=True, to='course.course', verbose_name='курсы студента'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lesson',
            field=models.ManyToManyField(blank=True, to='lesson.lesson', verbose_name='уроки студента'),
        ),
    ]
