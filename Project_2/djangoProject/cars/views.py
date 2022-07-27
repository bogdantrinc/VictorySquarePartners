from django.shortcuts import get_object_or_404, render
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


# Create your views here.
