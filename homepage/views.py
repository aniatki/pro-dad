from django.shortcuts import render
from django.views import generic
from .models import Package


class PackageList(generic.ListView):
    model = Package
    template_name = 'index.html'
    
def home():
    return 