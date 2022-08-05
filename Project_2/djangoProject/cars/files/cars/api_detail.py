import requests
account = {
    "email": "test.test@victorysquarepartners.com",
    "password": "Y4WUzqYFu3Dif8K",
    'content-type': 'application/json'
}


def api_detail(vin: str):
    """
    Gets data about a car from an API based on a vin.
    :param vin: A string resembling a vin used to fetch data about a car.
    :return: A dictionary containing data about a car.
    """
    get_token = requests.post('https://api.dev.carfeine.net/auth/login', account)
    token = get_token.json()['token']
    header = {
        'Authorization': f'Token {token}',
        'content-type': 'application/json',
    }
    data = {
        "vehicles": [{"vin": vin}],
    }
    get_vin = requests.post('https://api.dev.carfeine.net/revin/tier1/describe-core/', headers=header, json=data)
    vin_url = get_vin.json()['vin_urls'][0]
    get_car_data = requests.get(vin_url, headers=header)
    car_data = get_car_data.json()['results'][0]['data']['core_attributes']
    return car_data


call = api_detail(vin='1GNSKPKD3MR214906')

print(call)
