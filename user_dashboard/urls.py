from . import views
from django.urls import path


urlpatterns = [
    path('user_dashboard/', views.user_dashboard ,name="user_dashboard")
]