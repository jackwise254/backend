# Generated by Django 4.1.4 on 2023-05-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0036_reactions_property'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactions',
            name='property',
        ),
    ]