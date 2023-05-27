import requests
import bot, market

interval = "1h"

'''
Simple GET request
'''
def get(url: str):
    response = requests.get(url) 
    if response.status_code!= 200:
        return None
    return response.json()


'''
Pair Example:
BTC/USDT
'''
def get_method_values(pair: str, method: str, exchange: str = 'binance'):
    interval = "5m"
    return get(f"https://api.taapi.io/{method}?secret={bot.keys.get('taapi')}&exchange={exchange}&symbol={pair}/USDT&interval={interval}") #TODO: fix conversion


'''
RSI Indicator
'''
def rsi(pair: str):
    d = get_method_values(pair=pair.split("/")[0], method='rsi')
    print(d.get('value'))

    if d.get('value') > 70: #Overbought => should sell
        return 'sell'
    if d.get('value') < 30: #Oversold => should buy
        return 'buy'
    return 'hold' #Neither detected => should hold


'''
Bollinger Bands Indicator
'''
def bbands2(pair: str):
    boundary = 0.02 #boundary is the safety number applied to lower and upper bounds

    #do everything to reduce the amount of requests per second
    d = get_method_values(pair=pair.split("/")[0], method='bbands2')
    price = market.get_price(pair)

    if d.get('valueUpperBand') * (1 - boundary) >= price:
        return 'sell'
    if d.get('valueLowerBand') * (1 + boundary) >= market.get_price(pair):
        return 'buy'

    return 'hold'

'''
Associate names with values
'''
functions = {
    'rsi': rsi,
    'bbands': bbands2
}