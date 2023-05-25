import requests, json
import settings

'''
Get price of coin
'''
def get_price(pair: str):
    id = settings.strats.get(pair).get('coingecko_id')
    convert = pair.split('/')[1]

    parameters = {
        'ids': id,
        'vs_currencies': convert,
    }
    headers = {
        'Accepts': 'application/json',
    }

    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?', params=parameters, headers=headers)
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(e)

print(get_price('ETH/USD'))