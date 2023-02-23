from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    fname = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        unique_together = (('username', 'email'))
        fields = ['username', 'fname', 'email', 'password1', 'password2']
        