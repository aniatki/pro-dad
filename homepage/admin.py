from django.contrib import admin
from .models import Package, Review, Booking

admin.site.register(Package)
admin.site.register(Review)
admin.site.register(Booking)