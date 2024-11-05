# Generated by Django 4.1.1 on 2024-10-09 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0004_remove_category_id_alter_category_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('lid', models.CharField(blank=True, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('ldate', models.DateField(default=django.utils.timezone.now)),
                ('language', models.CharField(max_length=255)),
            ],
        ),
    ]
