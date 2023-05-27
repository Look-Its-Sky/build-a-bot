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