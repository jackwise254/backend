# Generated by Django 4.1.4 on 2023-05-29 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_profile'),
        ('properties', '0050_delete_reactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('flags', models.IntegerField(default=0)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
