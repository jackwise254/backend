# Generated by Django 3.2.13 on 2023-04-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
