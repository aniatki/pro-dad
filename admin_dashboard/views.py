from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Package
from .forms import AddPackageForm
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, "admin_dashboard/admin_dashboard.html", {"title":"Admin Dashboard", 'request': request, 'bookings': bookings})


@login_required
def admin_packages(request):
    packages = Package.objects.all()
    form = AddPackageForm()
    
    context = {
        'title': 'Packages',
        'packages': packages,
        'form': form
    }

    if request.method == 'POST':
        form = AddPackageForm(request.POST, request.FILES)
        if form.is_valid():
            package_name = request.POST.get('name')
            form.save()
            messages.add_message(request, messages.SUCCESS, f'Item <strong>{package_name}</strong> added successfully.')
            return redirect('admin_packages')
        else:
            form = AddPackageForm
            if form.errors:
                messages.add_message(request, messages.WARNING, "Price can not be a negative value.")

    return render(request, 'admin_dashboard/admin_packages.html', context)


def delete_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    package.delete()
    messages.add_message(request, messages.SUCCESS, f'{package} was deleted.')
    return redirect('admin_packages')


def update_package(request, package_id):
    package = Package.objects.get(pk=package_id)
    form = AddPackageForm(request.POST and request.FILES or None, instance=package)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, f'{package} was updated.')
        return redirect('admin_packages')
    context = {
        'title': f'Edit {package.name}',
        'package': package,
        'form': form
    }
    return render(request, 'admin_dashboard/update_package.html', context)