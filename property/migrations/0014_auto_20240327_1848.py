# Generated by Django 2.2.24 on 2024-03-27 15:48
import phonenumbers

from django.db import migrations

def phone_parse(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        phone_number_parse = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phone_number_parse):
            phone_number = phonenumbers.format_number(phone_number_parse, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_pure_phone = phone_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(phone_parse),
    ]