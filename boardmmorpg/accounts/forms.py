from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AuthorUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = AuthorUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",

        )

class ActivationForm(forms.Form):
    email= forms.EmailField()
    code= forms.CharField(max_length=4)
#