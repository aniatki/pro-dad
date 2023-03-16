from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin_dashboard.forms import DateForm


@login_required
def user_dashboard(request):
    return render(request, "user_dashboard/user_dashboard.html", {
        "title": f"{request.user}'s Dashboard",
        })


