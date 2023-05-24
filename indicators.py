import requests

with open('api.txt', 'r') as f:
    api_key = f.readline()    
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
    return get("https://api.taapi.io/{method}?secret={api_key}&exchange={exchange}&symbol={pair}&interval={interval}")

'''
RSI Indicator
'''
def rsi(pair: str):
    d = get_method_values(pair, 'rsi')

    if d.get('value') > 70: #Overbought => should sell
        return 'sell'
    if d.get('value') < 30: #Oversold => should buy
        return 'buy'
    return 'hold' #Neither detected => should hold


'''
Associate names with values
'''
functions = {
    'rsi': rsi(),
}