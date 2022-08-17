from django.contrib import admin
from cars.models import Car
from cars.views import detail_list


class CarAdmin(admin.ModelAdmin):
    list_display = ('vin', 'make', 'model', 'date_added', 'described')
    list_filter = ['date_added', 'make', 'model']
    search_fields = ['vin', 'make', 'model']
    car_information = ['make', 'model'] + detail_list
    fieldsets = [
        (None, {'fields': ['vin']}),
        ('Car Information', {'fields': car_information}),
    ]
    add_fieldsets = fieldsets


admin.site.register(Car, CarAdmin)


# Register your models here.
