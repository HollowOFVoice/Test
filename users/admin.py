from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Создаем кастомный класс для админки
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'full_name')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительные данные', {'fields': ('phone', 'full_name', 'address')}),
    )

# Регистрируем только если модель еще не зарегистрирована
if not admin.site.is_registered(CustomUser):
    admin.site.register(CustomUser, CustomUserAdmin)