# Generated by Django 4.0.6 on 2022-07-26 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_vin',
                 models.CharField(error_messages={'unique': 'This car VIN already exists.'}, max_length=17, unique=True,
                                  validators=[django.core.validators.MinLengthValidator(17,
                                                                                        'The car VIN has a 17 characters format!'),
                                              django.core.validators.RegexValidator('^[a-zA-Z0-9]*$',
                                                                                    'The car VIN has only letters and numbers!')])),
                ('car_maker', models.CharField(default='No data.', max_length=100)),
                ('car_model', models.CharField(default='No data.', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
    ]
