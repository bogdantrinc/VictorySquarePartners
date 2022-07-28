from django.shortcuts import get_object_or_404, render
from django.views import generic
from cars.models import Car


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


def more_details(request, pk):
    car = get_object_or_404(Car, pk=pk)
    try:
        car_detail = Car.objects.filter(pk=pk).values()[0]
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
