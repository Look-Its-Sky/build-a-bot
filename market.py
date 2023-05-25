import requests, json
from bot import keys

def get_cmc_listings():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': keys['coinmarketcap']
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        data = json.loads(response.text)
        print(data)
    except requests.exceptions.RequestException as e:
        print(e)