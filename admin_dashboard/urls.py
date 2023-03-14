from . import views
from django.urls import path

urlpatterns = [
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('admin_packages', views.admin_packages, name="admin_packages"),

]