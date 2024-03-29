# Generated by Django 3.1.3 on 2021-11-18 14:10

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0017_person_is_dark_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефона'),
        ),
    ]
