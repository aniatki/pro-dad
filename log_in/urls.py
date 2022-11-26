from . import views
from django.urls import path

urlpatterns = [
    path('log_in/', views.log_in, name="log_in")
]