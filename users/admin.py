from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_premium')
    list_filter = ('is_staff', 'is_active', 'is_premium')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
