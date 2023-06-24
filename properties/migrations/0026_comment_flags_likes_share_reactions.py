# Generated by Django 4.1.4 on 2023-05-29 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_profile'),
        ('properties', '0025_property_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('total_comments', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_flags', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('total_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('total_shares', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.comment')),
                ('flags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.flags')),
                ('likes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.likes')),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
                ('shares', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.share')),
            ],
        ),
    ]
