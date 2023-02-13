from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    (10, "Excellent")
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


class Reviews(models.Model):
    rating = models.IntegerField(choices=RANGE_1_TO_10)
    slug = models.SlugField(max_length=200, unique=True)
    fname = models.CharField(max_length=50)
    body = models.TextField()
    avatar = CloudinaryField('image', default='placeholder')
