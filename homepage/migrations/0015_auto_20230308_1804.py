# Generated by Django 3.2.16 on 2023-03-08 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_auto_20230305_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='slug',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='fname',
            new_name='name',
        ),
    ]
