# Generated by Django 4.1.4 on 2023-05-29 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_property_area_property_baths_property_coverphoto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='area',
        ),
    ]
