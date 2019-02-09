from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username','organizations')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('organizations', 'password')