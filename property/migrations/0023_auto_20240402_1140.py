# Generated by Django 2.2.24 on 2024-04-02 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20240329_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]