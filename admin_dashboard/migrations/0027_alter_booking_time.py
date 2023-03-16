# Generated by Django 3.2.16 on 2023-03-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0026_remove_booking_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('0900', '09:00'), ('1030', '10:30'), ('1200', '12:00'), ('1530', '15:30'), ('1700', '17:00')], max_length=5),
        ),
    ]
