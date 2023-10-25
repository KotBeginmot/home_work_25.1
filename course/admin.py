from django.contrib import admin

from course.models import Course, Payments, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description' , 'id']


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'user', 'paid']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'subscription']
