from django.contrib import admin

from lesson.models import Lesson


@admin.register(Lesson)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['course','id', 'name', 'description', 'video_link']
