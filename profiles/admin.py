from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Профиль пользователя"""
    list_display = ('author', 'status', 'image', 'slug', 'create_data',)
    save_on_top = True


