from django.contrib import admin
from .models import Package, Review, AppointmentTime, Booking

admin.site.register(Package)
admin.site.register(Review)
admin.site.register(AppointmentTime)
admin.site.register(Booking)