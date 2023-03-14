from . import views
from django.urls import path


urlpatterns = [
    path('sign_up/', views.sign_up, name="sign_up"),
    path('log_in/', views.log_in, name="log_in"),
    path('log_out/', views.log_out, name='log_out'),
]