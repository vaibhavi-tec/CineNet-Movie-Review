# Generated by Django 4.1.1 on 2024-10-09 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0005_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('mimage', models.ImageField(blank=True, upload_to='images/')),
                ('mid', models.CharField(blank=True, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('director', models.TextField()),
                ('writer', models.TextField()),
                ('stars', models.TextField()),
                ('reviews', models.TextField()),
                ('year', models.PositiveIntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('cast', models.ImageField(blank=True, upload_to='images/')),
                ('movie_link', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]