# Generated by Django 5.0.6 on 2024-06-06 01:41

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_currency_user_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
