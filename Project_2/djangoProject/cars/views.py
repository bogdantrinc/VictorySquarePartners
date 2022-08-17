from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from requests.exceptions import JSONDecodeError
from accounts.forms import RegisterUser, EditUser
from cars.files.cars.api_detail import api_detail
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


class EditUser(generic.UpdateView):
    form_class = EditUser
    template_name = "cars/account/profile.html"
    success_url = reverse_lazy('cars:index')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "You've updated your profile successfully!")
        return super().form_valid(form)


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'cars/account/password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "You've changed your password successfully!")
        return super().form_valid(form)


def more_details(request, pk):
    car_queryset = Car.objects.filter(pk=pk)
    try:
        car = car_queryset.first()
        if not car.described:
            get_api_data = api_detail(car.vin)
            api_data = {key: value for key, value in get_api_data.items() if value is not None}
            get_car_detail = Car.objects.filter(pk=pk).values()[0]
            for detail_name in get_car_detail:
                if detail_name in api_data:
                    setattr(car, detail_name, api_data[detail_name])
            car.described = True
            car.save()
        car_detail = car_queryset.values(*detail_list)[0]

    except JSONDecodeError:
        messages.error(request, "Couldn't fetch more data from the server.")
        return render(request, 'cars/detail.html', {
            'car': car,
        })

    except (Car.DoesNotExist, IndexError):
        raise Http404("Car does not exist!")

    else:
        return render(request, 'cars/detail.html', {
            'car': car,
            'car_detail': car_detail
        })

def register_request(request):
	if request.method == "POST":
		form = RegisterUser(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("cars:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterUser()
	return render(request=request, template_name="cars/account/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("cars:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="cars/account/login.html", context={"login_form": form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/login/")
