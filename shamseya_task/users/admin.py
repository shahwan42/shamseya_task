from django.contrib import admin, auth

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ["email", "username"]
