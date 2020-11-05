from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import get_user_model

from .forms import UserCreationForm, UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ["email", "username"]
