import requests
import bot

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
Associate names with values
'''
functions = {
    'rsi': rsi,
}