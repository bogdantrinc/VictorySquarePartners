# Generated by Django 4.1 on 2022-08-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_premium',
            field=models.BooleanField(default=False, verbose_name='Premium'),
        ),
    ]
