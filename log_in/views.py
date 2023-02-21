from django.shortcuts import render


def log_in(request, *args):
    return render(request, "log_in/log_in.html", {"title": "Log In"})