# Generated by Django 3.2.16 on 2022-11-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
