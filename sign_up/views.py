from django.shortcuts import render


def sign_up(request):
    return render(request, "sign_up/sign_up.html", {"title": "Sign Up"})