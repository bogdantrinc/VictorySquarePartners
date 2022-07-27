# Generated by Django 4.0.6 on 2022-07-27 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='availability',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='body_style',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='car_trim',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='cylinders',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='car',
            name='displacement',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='exterior_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_economy_city',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_economy_city_unit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_economy_highway',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_economy_highway_unit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='grouped_body_style',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='grouped_exterior_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='grouped_interior_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='grouped_transmission_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='interior_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage_unit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='msrp',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='car',
            name='normalized_make',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='sale_price',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='car',
            name='state_of_vehicle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='stock_number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1900)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_maker',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_vin',
            field=models.CharField(error_messages={'unique': 'This car VIN already exists.'}, max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17, 'The car VIN has a 17 characters format!'), django.core.validators.RegexValidator('^[A-Z0-9]*$', 'The car VIN has only numbers and capital letters!')]),
        ),
    ]
