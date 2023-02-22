from django.shortcuts import render, redirect
from .forms import RegisterForm


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
        
    return render(request, "sign_up/sign_up.html", {"title": "Sign Up", "form": form})