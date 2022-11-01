from dataclasses import field
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "last_name",
            "first_name",
            "email",
            "image",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
