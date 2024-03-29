# Generated by Django 3.2.16 on 2023-03-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0011_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Extremely Low'), (2, 'Very Low'), (3, 'Low'), (4, 'Moderately Low'), (5, 'Moderate'), (6, 'Moderately High'), (7, 'High'), (8, 'Very High'), (9, 'Extremely High'), (10, 'The Highest')])),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
    ]
