# Generated by Django 4.1.4 on 2023-05-29 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0037_remove_reactions_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='propert',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='properties.property'),
            preserve_default=False,
        ),
    ]
