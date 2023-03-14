from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_dashboard(request, **kwargs):
    return render(request, "user_dashboard/user_dashboard.html", {"title": f"{kwargs}'s Dashboard"})