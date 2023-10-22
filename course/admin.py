from django.contrib import admin

from course.models import Course, Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'user', 'paid']
