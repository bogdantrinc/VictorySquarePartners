from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator, MinValueValidator
from django.utils import timezone


class Car(models.Model):
    car_vin = models.CharField(max_length=17, unique=True,
                               error_messages={"unique": "This car VIN already exists."},
                               validators=[MinLengthValidator(17, "The car VIN has a 17 characters format!"),
                                           RegexValidator(r'^[A-Z0-9]*$',
                                                          'The car VIN has only numbers and capital letters!')])
    date_added = models.DateTimeField('date added', auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500, default='')
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(timezone.now().year),
                                                        MinValueValidator(1900)],
                                            null=True)
    car_maker = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_trim = models.CharField(max_length=100, default='')
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
        return self.car_vin

    # def detail(self):
    #     detail = Car.objects.filter(pk=self.id).values()[0]
    #     clear_detail = {}
    #     for name_detail, detail in detail.items():
    #         if detail and detail != 'No data.':
    #             clear_detail[name_detail] = detail
    #     return clear_detail


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_vin', 'car_maker', 'car_model', 'date_added')
    list_filter = ['date_added', 'car_maker', 'car_model']
    search_fields = ['car_vin', 'car_maker', 'car_model']
    fieldsets = [
        (None, {'fields': ['car_vin']}),
        ('Car Information', {'fields': ['car_maker', 'car_model']}),
    ]

# Create your models here.
