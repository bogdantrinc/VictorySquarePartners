import requests
from django.conf import settings


def api_detail(vin: str):
    """
    Gets data about a car from an API based on a vin.
    :param vin: A string resembling a vin used to fetch data about a car.
    :return: A dictionary containing data about a car.
    """
    get_token = requests.post(settings.API_URL_AUTH, {"email": settings.API_ACCOUNT_EMAIL,
                                                      "password": settings.API_ACCOUNT_PASSWORD})
    token = get_token.json()['token']
    header = {
        'Authorization': f'Token {token}',
        'content-type': 'application/json',
    }
    data = {
        "vehicles": [{"vin": vin}],
    }
    get_vin = requests.post(settings.API_URL_DESCRIBE, headers=header, json=data)
    vin_url = get_vin.json()['vin_urls'][0]
    get_car_data = requests.get(vin_url, headers=header)
    car_data = get_car_data.json()['results'][0]['data']['core_attributes']
    return car_data
