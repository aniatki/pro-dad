from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from django.utils import timezone



STATUS = ((0, "Draft"), (1, "Published"))
RANGE_1_TO_10 = (
    (1, "Extremely Low"),
    (2, "Very Low"),
    (3, "Low"),
    (4, "Moderately Low"),
    (5, "Moderate"),
    (6, "Moderately High"),
    (7, "High"),
    (8, "Very High"),
    (9, "Extremely High"),
    (10, "The Highest")
)

class Package(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    length = models.IntegerField(choices=RANGE_1_TO_10)
    timeframe = models.IntegerField(choices=RANGE_1_TO_10)
    thickness = models.IntegerField(choices=RANGE_1_TO_10)
    endurance = models.IntegerField(choices=RANGE_1_TO_10)
    image_url = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(choices=RANGE_1_TO_10)
    slug = models.SlugField(max_length=200)
    fname = models.CharField(max_length=50)
    body = models.TextField(default=timezone.now)
    
    def __str__(self):
        return self.rating


class Booking(models.Model):
    APPOINTMENT_TIMES = [
        ('0900', '09:00'),
        ('1030', '10:30'),
        ('1200', '12:00'),
        ('1530', '15:30'),
        ('1700', '17:00'),
    ]
    booked_at = models.DateField(auto_now_add=True, blank=False)
    customer_name = models.CharField(max_length=50)
    time = models.CharField(max_length=4, choices=APPOINTMENT_TIMES)
    date = models.DateField(blank=False, default=timezone.now)
    
    def __str__(self):
        return self.date.strftime("%m/%d/%Y")
