# Generated by Django 4.1.1 on 2024-10-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('uid', models.CharField(blank=True, editable=False, max_length=100, unique=True)),
                ('username', models.CharField(blank=True, default='User', max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=255)),
            ],
        ),
    ]
