from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard/admin_dashboard.html", {"title":"Admin Dashboard"})


@login_required
def admin_packages(request):
    return render(request, 'admin_dashboard/admin_packages.html', {"title": "Packages"})