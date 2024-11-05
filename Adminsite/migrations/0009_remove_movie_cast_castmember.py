# Generated by Django 4.1.1 on 2024-10-16 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0008_movie_stars_alter_movie_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
        migrations.CreateModel(
            name='CastMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast', models.CharField(max_length=100)),
                ('cimage', models.ImageField(upload_to='images/cast_images/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast_members', to='Adminsite.movie')),
            ],
        ),
    ]