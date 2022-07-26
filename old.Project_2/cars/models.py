from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, RegexValidator


class Car(models.Model):
    car_vin = models.CharField(max_length=17, unique=True,
                               error_messages ={"unique":"This car VIN already exists."},
                               validators=[MinLengthValidator(17, "The car VIN has a 17 characters format!"),
                                           RegexValidator(r'^[a-zA-Z0-9]*$', 'The car VIN has only letters and numbers!')])
    car_maker = models.CharField(max_length=100, default='No data.')
    car_model = models.CharField(max_length=100, default='No data.')
    date_added = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return self.car_vin


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_vin', 'car_maker', 'car_model', 'date_added')
    list_filter = ['date_added', 'car_maker', 'car_model']
    search_fields = ['car_vin', 'car_maker', 'car_model']
    fieldsets = [
        (None, {'fields': ['car_vin']}),
        ('Car Information', {'fields': ['car_maker', 'car_model']}),
    ]


# Create your models here.
