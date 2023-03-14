from django.contrib import admin
from django.urls import path, include
import homepage.urls, admin_dashboard.urls, user_dashboard.urls, authenticate.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage.urls)),
    path('', include(admin_dashboard.urls)),
    path('', include(authenticate.urls)),
    path('', include(user_dashboard.urls)),
]
