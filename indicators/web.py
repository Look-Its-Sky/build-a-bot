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
