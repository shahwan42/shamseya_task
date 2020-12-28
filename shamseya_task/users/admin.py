from django.contrib import admin, auth

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = (
        "id",
        "username",
        "email",
        "name",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    list_display_links = ("id",)
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "name")
    ordering = ("-id",)

    fieldsets = (
        (
            None,
            {"fields": ("email", "name", "password")},
        ),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
