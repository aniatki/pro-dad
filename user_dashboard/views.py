from django.shortcuts import render


def user_dashboard(request, **kwargs):
    return render(request, "user_dashboard/user_dashboard.html", {"title": f" {kwargs}'s Dashboard"})