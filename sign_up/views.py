from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    context = {'form'}
    return render(request, "sign_up/sign_up.html", {"title": "Sign Up"})