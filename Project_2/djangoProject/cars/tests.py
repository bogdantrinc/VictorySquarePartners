from django.test import TestCase
from django.urls import reverse

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


# Create your tests here.
