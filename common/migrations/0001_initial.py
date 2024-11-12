# Generated by Django 4.2.4 on 2024-11-05 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'airline',
            },
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'car_type',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_currency', models.CharField(max_length=3)),
                ('rate', models.DecimalField(decimal_places=6, max_digits=20)),
                ('date_fetched', models.DateTimeField(default=django.utils.timezone.now)),
                ('next_update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'exchange_rate',
            },
        ),
        migrations.CreateModel(
            name='HotelDailyBaseRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'hotel_daily_base_rate',
            },
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'meal_category',
            },
        ),
        migrations.CreateModel(
            name='MileageRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=3, unique=True)),
                ('title', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'mileage_rate',
            },
        ),
        migrations.CreateModel(
            name='RelationshipToPAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'relationship_to_pai',
            },
        ),
        migrations.CreateModel(
            name='RentalAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'rental_agency',
            },
        ),
    ]
