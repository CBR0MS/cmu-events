# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username',]
    fieldsets = ((None, {
            'fields': ('first_name', 'last_name', 'organizations', )
        }),)

admin.site.register(User, CustomUserAdmin)