from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from cars.views import detail_list
from cars.models import Car


class CarIndexViewTests(TestCase):
    def test_no_cars(self):
        """
        If no cars exist, an apropriate message is displayed.
        """
        Car.objects.all().delete()
        response = self.client.get(reverse('cars:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['car_list'], [])

    def test_two_cars(self):
        """
        If two cars are in the database, only two cars should be displayed.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='3GNKBKRS1LS573917')
        car2 = Car.objects.create(vin='1GNSCNKD8MR429859')
        response = self.client.get(reverse('cars:index'))
        self.assertQuerysetEqual(response.context['car_list'], [car1, car2], ordered=False)

    def test_incorrect_vin_format(self):
        """
        If ValidationError is raised, the car is not in the list.
        """
        Car.objects.all().delete()
        with self.assertRaises(ValidationError):
            car2 = Car(vin='@123456789ABCDEFG')
            car2.full_clean(exclude=detail_list)
            car2.save()
        response = self.client.get(reverse('cars:index'))
        self.assertContains(response, "No cars are available.")
        self.assertQuerysetEqual(response.context['car_list'], [])


class CarDetailViewTests(TestCase):
    def test_details(self):
        """
        The page should show the proper vin.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='3GNKBKRS1LS573917')
        url = reverse('cars:detail', args=(car1.id,))
        response = self.client.get(url)
        self.assertContains(response, car1.vin)

    def test_details_same_as_created(self):
        """
        The page should show basic details of a car.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='4T1KZ1AK5MU050696', make='Toyota', model='Camry')
        url = reverse('cars:detail', args=(car1.id,))
        response = self.client.get(url)
        self.assertContains(response, '4T1KZ1AK5MU050696')
        self.assertContains(response, 'Toyota')
        self.assertContains(response, 'Camry')


class MoreDetailsViewTests(TestCase):
    def test_more_details(self):
        """
        The page should show more details of a car.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='3GNKBKRS1LS573917',
                                  title='test',
                                  description='test',
                                  year=timezone.now().year,
                                  trim='test',
                                  mileage=1,
                                  mileage_unit='test',
                                  transmission_type='test',
                                  fuel_type='test',
                                  body_style='test',
                                  drivetrain='test',
                                  interior_color='test',
                                  exterior_color='test',
                                  doors=1,
                                  cylinders=1,
                                  displacement='test',
                                  msrp=0.1,
                                  state_of_vehicle='test',
                                  grouped_exterior_color='test',
                                  grouped_interior_color='test',
                                  engine='test',
                                  fuel_economy_city=1,
                                  fuel_economy_city_unit='test',
                                  fuel_economy_highway=1,
                                  fuel_economy_highway_unit='test',
                                  availability=True,
                                  image_url='http://127.0.0.1:8000/cars/',
                                  normalized_make='test',
                                  grouped_body_style='test',
                                  grouped_transmission_type='test',
                                  sale_price=0.1,
                                  url='http://127.0.0.1:8000/cars/',
                                  stock_number=1,
                                  )
        url = reverse('cars:more', args=(car1.id,))
        response = self.client.get(url)
        for attribute in detail_list:
            self.assertContains(response, getattr(car1, attribute))

    def test_more_details_errors(self):
        """
        The page should return error code 404.
        """
        Car.objects.all().delete()
        url = reverse('cars:more', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


# Create your tests here.
