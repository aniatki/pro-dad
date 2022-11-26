from django.shortcuts import render

# Create your views here.
def admin_packages(request):
    return render(request, 'admin_packages/admin_packages.html', {"title": "Admin Packages"})