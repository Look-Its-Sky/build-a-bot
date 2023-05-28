import requests
import bot, market

interval = "1h"
results = {
    'buy': [],
    'sell': [],
    'hold': []
}


'''
Simple GET request
'''
def get(url: str):
    try:
        response = requests.get(url) 
    except requests.exceptions.ConnectionError:
        return None

    if response.status_code!= 200:
        return None
    return response.json()


'''
Get value of indicator GET request
'''
def get_method_values(pair: str, method: str, exchange: str = 'binance'):
    interval = "5m"
    return get(f"https://api.taapi.io/{method}?secret={bot.keys.get('taapi')}&exchange={exchange}&symbol={pair}/USDT&interval={interval}") #TODO: fix conversion


'''
RSI Indicator
'''
def rsi(pair: str):
    overbought = 65 #lets go aggressive 😈
    oversold = 45

    result = 'hold'
    d = get_method_values(pair=pair.split("/")[0], method='rsi')
    if not d.get('valueUpperBand') or not d.get('valueLowerBand'):
        return 'hold (api error)' #API error
    rsi = d.get('value')

    if rsi >= overbought: #Overbought => should sell
        result = 'sell'
    if rsi < oversold: #Oversold => should buy
        result = 'buy'
    
    results[result].append('rsi')
    return result #Neither detected => should hold


'''
Bollinger Bands Indicator
'''
def bbands2(pair: str):
    boundary = 0.02
    result = 'hold'

    d = get_method_values(pair=pair.split("/")[0], method='bbands2')
    if not d or not d.get('valueUpperBand') or not d.get('valueLowerBand'):
        return 'hold (api error)' #API error

    price = market.get_price(pair)
    print(price)

    if d.get('valueUpperBand') * (1 - boundary) >= price: #Overbought => should sell
        result = 'sell'
    
    if d.get('valueLowerBand') * (1 + boundary) >= price: #Oversold => should buy
        result = 'buy'

    results[result].append('bbands2')
    return result


'''
Associate names with values
'''
functions = {
    'rsi': rsi,
    'bbands2': bbands2
}