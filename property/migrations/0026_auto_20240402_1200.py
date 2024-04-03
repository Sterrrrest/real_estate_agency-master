# Generated by Django 2.2.24 on 2024-04-02 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_auto_20240402_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owned_by',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complained_flats', to='property.Flat', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complained_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_flats',
            field=models.ManyToManyField(blank=True, related_name='owned_by', to='property.Flat', verbose_name='Владеет квартирами'),
        ),
    ]