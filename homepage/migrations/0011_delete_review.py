# Generated by Django 3.2.16 on 2023-03-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_delete_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]