import web

'''
Timeout for broke boi plan
'''
taapi_timeout = 15

'''
Get value of indicator GET request 
for TAAPI
'''
def get_method_values(ticker: str, method: str, exchange: str = 'binance'):
    time.sleep(taapi_timeout) #satisfy the api NOTE: implement a better timeout system
    url = f"https://api.taapi.io/{method}?secret={settings.keys.get('taapi')}&exchange={exchange}&symbol={ticker}/USDT&interval={interval}"
    return web.get(url) #TODO: fix conversion


'''
Get value of indicator POST request
for TAAPI (currently unused)
'''
def post_method_values(pair: str, exchange: str = 'binance'):
    time.sleep(taapi_timeout)
    return web.post("https://api.taapi.io/bulk", data= {
        'secret': settings.keys.get('taapi'),
        'construct': {
            'exchange': exchange,
            'symbol': pair,
            'interval': interval,
            'indicators': settings.indicators
        },
    }).text
 
