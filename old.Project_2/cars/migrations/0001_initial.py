# Generated by Django 4.0.6 on 2022-07-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_vin', models.CharField(max_length=17)),
                ('cars_brand', models.CharField(max_length=100)),
                ('cars_model', models.CharField(max_length=100)),
            ],
        ),
    ]
