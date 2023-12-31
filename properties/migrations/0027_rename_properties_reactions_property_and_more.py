# Generated by Django 4.1.4 on 2023-05-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0026_comment_flags_likes_share_reactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reactions',
            old_name='properties',
            new_name='property',
        ),
        migrations.AlterField(
            model_name='reactions',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='flags',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reactions',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]
