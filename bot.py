import indicators, settings, market.alpaca
import json
from datetime import datetime

'''
Runs every <wait time> (should be at least 15 seconds by default) due to all of the free api limitations
'''
def update(pair: str, strategy: object, current_market: object):
    result = strategy.update(pair, current_market)

    if result == 'buy':
        current_market.buy_mo(pair)

    if result == 'sell':
        current_market.sell_mo(pair)
