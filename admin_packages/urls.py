from . import views
from django.urls import path


urlpatterns = [
    path('admin_packages/', views.admin_packages, name="admin_packages")
]