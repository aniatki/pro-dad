from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking


@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, "admin_dashboard/admin_dashboard.html", {"title":"Admin Dashboard", 'request': request, 'bookings': bookings})


@login_required
def admin_packages(request):
    return render(request, 'admin_dashboard/admin_packages.html', {"title": "Packages"})