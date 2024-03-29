from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from django.utils import timezone
from django.core.validators import MinValueValidator



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
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    length = models.IntegerField(choices=RANGE_1_TO_10)
    timeframe = models.IntegerField(choices=RANGE_1_TO_10)
    thickness = models.IntegerField(choices=RANGE_1_TO_10)
    endurance = models.IntegerField(choices=RANGE_1_TO_10)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.name

    def alt_text(self):
        return self.name + ' Preview'

    def url(self):
        return self.slug

    def slug(self):
        nlist = self.name.casefold().split(' ') 
        return '-'.join(nlist)



class Review(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RANGE_1_TO_10)
    header = models.CharField(max_length=200)
    body = models.TextField(max_length=1000, blank=False)
    date=models.DateField(default=timezone.now, blank=False)
    
    def __str__(self):
        return str(self.rating)


class Booking(models.Model):
    APPOINTMENT_TIMES = [
        ('09:00', '0900'),
        ('10:30', '1030'),
        ('12:00', '1200'),
        ('15:30', '1530'),
        ('17:00', '1700'),
    ]
    booked_at = models.DateField(auto_now_add=True, blank=False)
    time = models.CharField(max_length=5, choices=APPOINTMENT_TIMES)
    date = models.DateField(blank=False, default=timezone.now)

    def __str__(self):
        return self.date.strftime("%m/%d/%Y")

