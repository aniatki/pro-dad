from django.shortcuts import render


def user_dashboard(request, *args):
    return render(request, "user_dashboard/user_dashboard.html", {"title": f"{args} Dashboard"})