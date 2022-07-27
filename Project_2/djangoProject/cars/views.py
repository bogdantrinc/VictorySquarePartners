from django.shortcuts import get_object_or_404
from django.views import generic
from cars.models import Car
import inspect


class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        """
        Return a list with cars.
        """
        return Car.objects.all()


class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'

    def get_queryset(self):
        return Car.objects.all()


def detail(request, car_id):
    """
    Return a list with all the valid attributes of a car.
    """
    car = get_object_or_404(Car, pk=car_id)
    car_details = []
    for _ in inspect.getmembers(car):
        if not _[0].startswith('_'):
            if not inspect.ismethod(_[1]):
                car_details.append(_)
    return car_details


# Create your views here.
