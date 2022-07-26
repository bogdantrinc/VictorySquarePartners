from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator, MinValueValidator
from django.utils import timezone


class Car(models.Model):
    car_vin = models.CharField(max_length=17, unique=True,
                               error_messages={"unique": "This car VIN already exists."},
                               validators=[MinLengthValidator(17, "The car VIN has a 17 characters format!"),
                                           RegexValidator(r'^[a-zA-Z0-9]*$',
                                                          'The car VIN has only letters and numbers!')])
    date_added = models.DateTimeField('date added', auto_now_add=True)
    title = models.CharField(max_length=100, default='No data.')
    description = models.TextField(max_length=500, default='No data.')
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(timezone.now().year),
                                                        MinValueValidator(1900)],
                                            default=timezone.now().year)
    car_maker = models.CharField(max_length=100, default='No data.')
    car_model = models.CharField(max_length=100, default='No data.')
    car_trim = models.CharField(max_length=100, default='No data.')
    mileage = models.PositiveSmallIntegerField(default=0)
    mileage_unit = models.CharField(max_length=100, default='No data.')
    transmission_type = models.CharField(max_length=100, default='No data.')
    fuel_type = models.CharField(max_length=100, default='No data.')
    body_style = models.CharField(max_length=100, default='No data.')
    drivetrain = models.CharField(max_length=100, default='No data.')
    interior_color = models.CharField(max_length=100, default='No data.')
    exterior_color = models.CharField(max_length=100, default='No data.')
    doors = models.PositiveSmallIntegerField(default=0)
    cylinders = models.PositiveSmallIntegerField(default=0)
    displacement = models.CharField(max_length=100, default='No data.')
    msrp = models.FloatField(max_length=100, validators=[MinValueValidator(0)], default=0)
    state_of_vehicle = models.CharField(max_length=100, default='No data.')
    grouped_exterior_color = models.CharField(max_length=100, default='No data.')
    grouped_interior_color = models.CharField(max_length=100, default='No data.')
    engine = models.CharField(max_length=100, default='No data.')
    fuel_economy_city = models.PositiveSmallIntegerField(default=0)
    fuel_economy_city_unit = models.CharField(max_length=100, default='No data.')
    fuel_economy_highway = models.PositiveSmallIntegerField(default=0)
    fuel_economy_highway_unit = models.CharField(max_length=100, default='No data.')
    availability = models.BooleanField(default=False)
    image_url = models.URLField(default=r'http://127.0.0.1:8000/cars/')
    normalized_make = models.CharField(max_length=100, default='No data.')
    grouped_body_style = models.CharField(max_length=100, default='No data.')
    grouped_transmission_type = models.CharField(max_length=100, default='No data.')
    sale_price = models.FloatField(max_length=100, validators=[MinValueValidator(0)], default=0)
    url = models.URLField(default=r'http://127.0.0.1:8000/cars/')
    stock_number = models.PositiveSmallIntegerField(default=0)

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
