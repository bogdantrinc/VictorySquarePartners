# Generated by Django 4.0.6 on 2022-07-29 11:55
import json

from django.db import migrations, IntegrityError


def refresh_data(apps, schema_editor):
    Car = apps.get_model('cars', 'Car')
    with open(r'C:\Users\Bogdan\PycharmProjects\VictorySquarePartners\Project_2\djangoProject\cars\templates\cars\hutto.json') as json_file:
        vin_list = json.load(json_file)
    for _ in vin_list:
        try:
            Car.objects.create(vin=_)
        except IntegrityError:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_car_maker_remove_car_car_model_and_more'),
    ]

    operations = [
        migrations.RunPython(refresh_data),
    ]
