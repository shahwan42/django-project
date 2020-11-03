from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as AuthUserCreationForm,
    UserChangeForm as AuthUserChangeForm,
)
from .models import User


class UserCreationForm(AuthUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(AuthUserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
