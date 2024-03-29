import requests, json, time
import bot, market, settings

interval = "5m"
results = {
    'buy': [],
    'sell': [],
    'hold': []
}
taapi_timeout = 15
current_price = None
last_price_request = None


'''
Simple GET request
'''
def get(url: str):
    sleep_time = 60

    try:
        response = requests.get(url) 
    except requests.exceptions.ConnectionError:
        return None

    if response.status_code == 429:
        print(f"We sent too many requests! Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)

    if response.status_code!= 200:
        print(f'Status code != 200\nStatus Code = {response.status_code}')
        return None
    return response.json()


'''
Simple POST request
'''
def post(url: str, data: json, exchange: str = 'binance'):
    init_data = {
        'secret': settings.keys.get('taapi')
    }

    init_data.update(data)
    return requests.post(url, json = init_data)


'''
Get value of indicator GET request
'''
def get_method_values(ticker: str, method: str, exchange: str = 'binance'):
    time.sleep(taapi_timeout) #satisfy the api NOTE: implement a better timeout system
    url = f"https://api.taapi.io/{method}?secret={settings.keys.get('taapi')}&exchange={exchange}&symbol={ticker}/USDT&interval={interval}"
    return get(url) #TODO: fix conversion


'''
Get value of indicator POST request
'''
def post_method_values(pair: str, exchange: str = 'binance'):
    time.sleep(taapi_timeout)
    return post("https://api.taapi.io/bulk", data= {
        'secret': settings.keys.get('taapi'),
        'construct': {
            'exchange': exchange,
            'symbol': pair,
            'interval': interval,
            'indicators': settings.indicators
        },
    }).text
                

'''
RSI Indicator
'''
def rsi(pair: str) -> str:
    overbought = 65 #lets go aggressive 😈
    oversold = 45

    result = 'hold'
    d = get_method_values(ticker=pair.split("/")[0], method='rsi')
    if not d.get('value'):
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
def bbands2(pair: str) -> str:
    boundary = 0.02
    result = 'hold'

    d = get_method_values(pair=pair.split("/")[0], method='bbands2')
    if d == None or not d.get('valueUpperBand') or not d.get('valueLowerBand'):
        return 'hold (api error)' #API error

    current_price = get_price(pair)

    if d.get('valueUpperBand') * (1 - boundary) >= current_price: #Overbought => should sell
        result = 'sell'
    
    if d.get('valueLowerBand') * (1 + boundary) >= current_price: #Oversold => should buy
        result = 'buy'

    results[result].append('bbands2')
    return result


'''
Triple Exponential Moving Average Indicator 
'''
def tema() -> str:
    boundary = 0.01 #the percentage over or under the boundary


'''
Get Price While Respecting Timeouts
'''
def get_price(pair: str) -> float:
    if not last_price_request or last_price_request - time.time() <= -15:
        return market.get_price(pair)
    return current_price
    

'''
Associate names with values
'''
functions = {
    'rsi': rsi,
    'bbands2': bbands2
}