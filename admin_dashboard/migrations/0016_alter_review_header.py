# Generated by Django 3.2.16 on 2023-03-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0015_auto_20230308_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='header',
            field=models.CharField(max_length=200),
        ),
    ]
