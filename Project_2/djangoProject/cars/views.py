from django.shortcuts import render
from django.views import generic
from cars.models import Car
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
        return Car.objects.all()

    # def refresh_data(self):
    #     with open(r'C:\Users\Bogdan\PycharmProjects\VictorySquarePartners\Project_2\djangoProject\cars\templates\cars\hutto.json') as json_file:
    #         car_vin_list = json.load(json_file)
    #     for _ in car_vin_list:
    #         try:
    #             Car.objects.create(car_vin=_)
    #         except django.db.IntegrityError:
    #             pass


class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'

    def get_queryset(self):
        return Car.objects.all()


def more_details(request, pk):
    car_queryset = Car.objects.filter(pk=pk)
    car = car_queryset.first()
    try:
        car_detail = car_queryset.values(*detail_list)[0]
    except (KeyError, Car.DoesNotExist):
        return render(request, 'cars/detail.html', {
            'car': car,
        })
    else:
        return render(request, 'cars/detail.html', {
            'car': car,
            'car_detail': car_detail
        })


# Create your views here.
