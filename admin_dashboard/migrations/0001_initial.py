# Generated by Django 3.2.16 on 2022-11-23 14:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('length', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('timeframe', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('thickness', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('endurance', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('image_url', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('avatar', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
    ]