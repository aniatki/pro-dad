# Generated by Django 3.2.16 on 2023-03-09 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0019_auto_20230309_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='image_url',
            new_name='image',
        ),
    ]