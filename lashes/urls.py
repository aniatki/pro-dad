from django.contrib import admin
from django.urls import path, include
import django.urls

print(django.urls)

import homepage.urls, admin_dashboard.urls, user_dashboard.urls, admin_packages.urls, authenticate.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage.urls)),
    path('', include(admin_dashboard.urls)),
    path('', include(authenticate.urls)),
    path('', include(user_dashboard.urls)),
    path('', include(admin_packages.urls)),
]
