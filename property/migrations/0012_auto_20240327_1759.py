# Generated by Django 2.2.24 on 2024-03-27 14:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20240327_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
