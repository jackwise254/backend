# Generated by Django 4.1.4 on 2023-05-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0031_remove_reactions_flags_remove_reactions_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='flags',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reactions',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]
