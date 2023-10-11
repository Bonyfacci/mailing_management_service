from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_staff', 'is_superuser', 'is_verified')
    list_filter = ('is_verified', 'is_staff')
    search_fields = ('email', 'phone', 'first_name', 'last_name')
