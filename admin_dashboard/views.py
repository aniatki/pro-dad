from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Package
from .forms import AddPackageForm
from django.contrib import messages



@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, "admin_dashboard/admin_dashboard.html", {"title":"Admin Dashboard", 'request': request, 'bookings': bookings})


@login_required
def admin_packages(request):
    """
    Create and Read functionality for serving the custom admin page
    """
    packages = Package.objects.all() # View all packages - Read
    
    # Add a package - Create
    form = AddPackageForm()
    if request.method == 'POST':
        form = AddPackageForm(request.POST, request.FILES)
        if form.is_valid():
            package_name = request.POST.get('name')
            form.save()
            messages.add_message(request, messages.SUCCESS, f'Item <strong>{package_name}</strong> added successfully.')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.WARNING, f'{field.value} {error}')
            form = AddPackageForm()

    return render(request, 'admin_dashboard/admin_packages.html', {"title": "Packages", 'packages':packages, 'form': form})

def delete_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    package.delete()
    messages.add_message(request, messages.SUCCESS, f'{package} was successfully deleted.')
    return redirect('admin_packages')

def update_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    
    messages.add_message(request, messages.SUCCESS, f'{package} was saved.')
    return redirect('admin_packages')