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
        The page should show basic details of a car.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='3GNKBKRS1LS573917')
        url = reverse('cars:detail', args=(car1.id,))
        response = self.client.get(url)
        self.assertContains(response, car1.vin)
        self.assertContains(response, car1.make)
        self.assertContains(response, car1.model)


class MoreDetailsViewTests(TestCase):
    def test_more_details(self):
        """
        The page should show more details of a car.
        """
        Car.objects.all().delete()
        car1 = Car.objects.create(vin='3GNKBKRS1LS573917',
                                  title='No data.',
                                  description='No data.',
                                  year=timezone.now().year,
                                  trim='No data.',
                                  mileage=1,
                                  mileage_unit='No data.',
                                  transmission_type='No data.',
                                  fuel_type='No data.',
                                  body_style='No data.',
                                  drivetrain='No data.',
                                  interior_color='No data.',
                                  exterior_color='No data.',
                                  doors=1,
                                  cylinders=1,
                                  displacement='No data.',
                                  msrp=0.1,
                                  state_of_vehicle='No data.',
                                  grouped_exterior_color='No data.',
                                  grouped_interior_color='No data.',
                                  engine='No data.',
                                  fuel_economy_city=1,
                                  fuel_economy_city_unit='No data.',
                                  fuel_economy_highway=1,
                                  fuel_economy_highway_unit='No data.',
                                  availability=True,
                                  image_url='http://127.0.0.1:8000/cars/',
                                  normalized_make='No data.',
                                  grouped_body_style='No data.',
                                  grouped_transmission_type='No data.',
                                  sale_price=0.1,
                                  url='http://127.0.0.1:8000/cars/',
                                  stock_number=1,
                                  )
        url = reverse('cars:more', args=(car1.id,))
        response = self.client.get(url)
        for _ in detail_list:
            self.assertContains(response, car1.__getattribute__(_))


# Create your tests here.
