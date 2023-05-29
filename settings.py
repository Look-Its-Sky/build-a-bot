import json

'''
Set all API keys
'''
with open('api.json', 'r') as f:
    keys = json.load(f)
    if not keys.get('taapi') or not keys.get('alpaca_api') or not keys.get('alpaca_secret'):
        print('Could not find all api keys\nexiting....')
        exit(-1)


'''
what indicators to use
'''
indicators = ['rsi', 'bbands2']


'''
when to sell what -- NOTE: we hate coingecko for this reason eventually fix ticker lookup in coingecko
'''
strats = {
    'ETH/USD': {
        'stop_loss': 2/100,
        'stop_price': 2/100,
        'coingecko_id': 'ethereum'
    },

    'BTC/USD': {
        'stop_loss': 2/100,
        'stop_price': 2/100,
        'coingecko_id': 'bitcoin'
    },
}