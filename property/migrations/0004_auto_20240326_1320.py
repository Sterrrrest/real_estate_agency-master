# Generated by Django 2.2.24 on 2024-03-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(),
        ),
    ]