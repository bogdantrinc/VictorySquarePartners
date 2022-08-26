from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.core.paginator import Paginator
from django.db.models import Q
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


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    redirect_field_name = None
    template_name = 'cars/index.html'
    context_object_name = 'car_list'
    paginate_by = 50
    model = Car

    def get_queryset(self):
        """
        Return a list with cars.
        """
        query = self.request.GET.get("vin")
        if query:
            vin_list = Car.objects.filter(Q(vin__contains=query) | Q(make__contains=query) | Q(model__contains=query))
        else:
            vin_list = Car.objects.all()
        return vin_list


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    redirect_field_name = None
    model = Car
    template_name = 'cars/detail.html'

    def get_queryset(self):
        return Car.objects.all()


class EditUser(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    login_url = 'login'
    redirect_field_name = None
    form_class = EditUser
    template_name = "cars/account/profile.html"
    success_url = reverse_lazy('cars:index')
    success_message = "You've updated your profile successfully!"

    def get_object(self):
        return self.request.user


class PasswordChange(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    login_url = 'login'
    redirect_field_name = None
    form_class = PasswordChangeForm
    template_name = 'cars/account/password.html'
    success_url = reverse_lazy('profile')
    success_message = "You've changed your password successfully!"


class PasswordReset(PasswordResetView):
    template_name = 'cars/account/password-reset/password_reset.html'
    email_template_name = 'cars/account/password-reset/password_reset_email.html'
    subject_template_name = 'cars/account/password-reset/password_reset_subject.txt'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.info(self.request, "If there is an account with this email, check your email for the reset password details!")
        return super().form_valid(form)


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'cars/account/password-reset/password_reset_confirm.html'
    success_url = reverse_lazy('cars:index')
    post_reset_login = True

    def dispatch(self, *args, **kwargs):
        dispatch = super().dispatch(*args, **kwargs)
        if not self.validlink and dispatch.status_code == 200:
            messages.error(self.request, "This password reset link has already been used.")
            return redirect('password_reset')
        return dispatch


@login_required(login_url='login', redirect_field_name=None)
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
				messages.info(request, f"You are now logged in as {username}")
				return redirect("cars:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="cars/account/login.html", context={"login_form": form})

@login_required(login_url='login', redirect_field_name=None)
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("login")

@login_required(login_url='login', redirect_field_name=None)
def delete_user_request(request):
    user = request.user
    logout(request)
    User = get_user_model()
    User.objects.filter(email=user.email).update(is_active=False)
    messages.success(request, f"You have successfully deleted your account: {user.email}")
    return redirect("cars:index")
