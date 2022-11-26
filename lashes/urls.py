from django.contrib import admin
from django.urls import path, include

import homepage.urls, log_in.urls, admin_dashboard.urls, sign_up.urls, user_dashboard.urls, admin_packages.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homepage.urls)),
    path('', include(log_in.urls)),
    path('', include(admin_dashboard.urls)),
    path('', include(sign_up.urls)),
    path('', include(user_dashboard.urls)),
    path('', include(admin_packages.urls)),
]
