# Generated by Django 2.2.24 on 2024-03-28 13:05

from django.db import migrations

def connect_flat_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    owners = Owner.objects.all()
    for owner in owners.iterator():
        flat_owner = Flat.objects.filter(owner=owner.owner)
        owner.owner_flats.set(flat_owner)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20240328_2328'),
    ]

    operations = [
        migrations.RunPython(connect_flat_owners),
    ]
