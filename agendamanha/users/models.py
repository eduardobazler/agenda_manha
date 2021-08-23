from django.contrib.auth.forms import UserCreationForm, UsernameField

from agendamanha.base.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {'username': UsernameField}
