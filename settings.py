import json

'''
Set all API keys
'''
with open('config.json', 'r') as f:
    keys = json.load(f)

if not keys.get('alpaca_api') or not keys.get('alpaca_secret'):
    print('Could not find all api keys\nexiting....')
    exit(-1)

if not keys.get('strategy'):
    print('Could not find strategy\nexiting....')
