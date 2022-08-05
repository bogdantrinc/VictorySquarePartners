from django.http import Http404
from django.shortcuts import render
from django.views import generic
from cars.models import Car
from cars.files.cars.api_detail import api_detail


get_detail_list = ['make', 'model', 'title', 'short_title', 'description', 'year', 'trim', 'mileage', 'mileage_unit',
                   'transmission_type', 'fuel_type', 'body_style', 'drivetrain', 'interior_color', 'exterior_color',
                   'doors', 'cylinders', 'displacement', 'msrp', 'state_of_vehicle', 'grouped_exterior_color',
                   'grouped_interior_color', 'engine', 'fuel_economy_city', 'fuel_economy_city_unit',
                   'fuel_economy_highway', 'fuel_economy_highway_unit', 'availability', 'image_url', 'normalized_make',
                   'grouped_body_style', 'grouped_transmission_type', 'sale_price', 'url', 'stock_number']


detail_list = ['title', 'description', 'year', 'trim', 'mileage', 'mileage_unit', 'transmission_type', 'fuel_type',
               'body_style', 'drivetrain', 'interior_color', 'exterior_color', 'doors', 'cylinders', 'displacement',
               'msrp', 'state_of_vehicle', 'grouped_exterior_color', 'grouped_interior_color', 'engine',
               'fuel_economy_city', 'fuel_economy_city_unit', 'fuel_economy_highway', 'fuel_economy_highway_unit',
               'availability', 'image_url', 'normalized_make', 'grouped_body_style', 'grouped_transmission_type',
               'sale_price', 'url', 'stock_number']




class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        """
        Return a list with cars.
        """
        query = self.request.GET.get("vin")
        if query:
            vin_list = Car.objects.filter(vin=query.upper())
        else:
            vin_list = Car.objects.all()
        return vin_list


class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'

    def get_queryset(self):
        return Car.objects.all()


def more_details(request, pk):
    car_queryset = Car.objects.filter(pk=pk)
    try:
        car = car_queryset.first()
        if not car.described:
            get_car_detail = car_queryset.values(*get_detail_list)[0]
            api_data = api_detail(car.vin)
            for detail_name in get_car_detail:
                if (detail_name in api_data) and api_data[detail_name]:
                    setattr(car, detail_name, api_data[detail_name])
            car.described = True
            car.save()
        car_detail = car_queryset.values(*detail_list)[0]

    except (Car.DoesNotExist, IndexError):
        raise Http404("Car does not exist!")
    else:
        return render(request, 'cars/detail.html', {
            'car': car,
            'car_detail': car_detail
        })


# Create your views here.
