# Generated by Django 4.1.4 on 2023-05-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0045_reactions_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]