# Generated by Django 4.1.4 on 2023-05-29 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0054_remove_property_comment_comment_agent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='property',
        ),
    ]