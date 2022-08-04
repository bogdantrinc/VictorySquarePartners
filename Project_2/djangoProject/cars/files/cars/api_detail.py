import requests
account = {
    "email": "test.test@victorysquarepartners.com",
    "password": "Y4WUzqYFu3Dif8K",
    'content-type': 'application/json'
}


def api_detail():
    get_token = requests.post('https://api.dev.carfeine.net/auth/login', account)
    token = get_token.json()['token']
    print(token)
    header = {
        'Authorization': f'Token {token}',
        'content-type': 'application/json',
    }
    data = {
        "vehicles": [{"vin": "1GNSCNKD8MR429859"}],
    }
    get_vin = requests.post('https://api.dev.carfeine.net/revin/tier1/describe-core/', headers=header, json=data)
    vin = get_vin.json()['vin_urls'][0]
    car_data = requests.get(vin, headers=header)
    return car_data


call = api_detail()

print(call.text)
