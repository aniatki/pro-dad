from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class RegisterForm(UserCreationForm):
    fname = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        unique_together = (('username', 'email'))
        fields = ['username', 'fname', 'email', 'password1', 'password2']

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

