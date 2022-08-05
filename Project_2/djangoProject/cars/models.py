from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator, MinValueValidator
from django.utils import timezone


class Car(models.Model):
    vin = models.CharField(max_length=17, unique=True, default='',
                           error_messages={"unique": "This car VIN already exists."},
                           validators=[MinLengthValidator(17, "The car VIN has a 17 characters format!"),
                                       RegexValidator(r'^[A-Z0-9]*$',
                                                      'The car VIN has only numbers and capital letters!')])
    date_added = models.DateTimeField('date added', auto_now_add=True)
    described = models.BooleanField(default=False)
    title = models.CharField(max_length=100, default='')
    short_title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500, default='')
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(timezone.now().year),
                                                        MinValueValidator(1900)],
                                            null=True)
    make = models.CharField(max_length=100, default='', blank=True)
    model = models.CharField(max_length=100, default='', blank=True)
    trim = models.CharField(max_length=100, default='')
    mileage = models.PositiveIntegerField(null=True)
    mileage_unit = models.CharField(max_length=100, default='')
    transmission_type = models.CharField(max_length=100, default='')
    fuel_type = models.CharField(max_length=100, default='')
    body_style = models.CharField(max_length=100, default='')
    drivetrain = models.CharField(max_length=100, default='')
    interior_color = models.CharField(max_length=100, default='')
    exterior_color = models.CharField(max_length=100, default='')
    doors = models.PositiveSmallIntegerField(null=True)
    cylinders = models.PositiveSmallIntegerField(null=True)
    displacement = models.CharField(max_length=100, default='')
    msrp = models.FloatField(validators=[MinValueValidator(0)], null=True)
    state_of_vehicle = models.CharField(max_length=100, default='')
    grouped_exterior_color = models.CharField(max_length=100, default='')
    grouped_interior_color = models.CharField(max_length=100, default='')
    engine = models.CharField(max_length=100, default='')
    fuel_economy_city = models.PositiveSmallIntegerField(null=True)
    fuel_economy_city_unit = models.CharField(max_length=100, default='')
    fuel_economy_highway = models.PositiveSmallIntegerField(null=True)
    fuel_economy_highway_unit = models.CharField(max_length=100, default='')
    availability = models.BooleanField(null=True)
    image_url = models.URLField(null=True)
    normalized_make = models.CharField(max_length=100, default='')
    grouped_body_style = models.CharField(max_length=100, default='')
    grouped_transmission_type = models.CharField(max_length=100, default='')
    sale_price = models.FloatField(validators=[MinValueValidator(0)], null=True)
    url = models.URLField(null=True)
    stock_number = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.vin


class CarAdmin(admin.ModelAdmin):
    list_display = ('vin', 'make', 'model', 'date_added', 'described')
    list_filter = ['date_added', 'make', 'model']
    search_fields = ['vin', 'make', 'model']
    fieldsets = [
        (None, {'fields': ['vin']}),
        ('Car Information', {'fields': ['make', 'model']}),
    ]

# Create your models here.
