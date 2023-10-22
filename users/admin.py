from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'user_phone']
    list_filter = ['is_active']
