from alpaca.trading.client import TradingClient
from alpaca.trading.requests import *
from alpaca.trading.enums import OrderSide, TimeInForce
import indicators, json, settings


'''
Set all API keys
'''
with open('api.json', 'r') as f:
    keys = json.load(f)
    if not keys.get('taapi') or not keys.get('alpaca_api') or not keys.get('alpaca_secret'):
        print('Could not find all api keys\nexiting....')
        exit(-1)  

alpaca_api = TradingClient(keys['alpaca_api'], keys['alpaca_secret'], paper=True)


'''
Market Order Buy Side
(Immediate Order)
'''
def buy_mo(pair: str):
    alpaca_api.submit_order(MarketOrderRequest(
        symbol = pair,
        side = OrderSide.BUY,
        time_in_force = TimeInForce.GTC,
        notional = 50,
        stop_loss = settings.strats[pair],
    ))


'''
Limit Order Buy Side
(Planned Order -- not in use yet)
'''
def buy_lo(pair: str, limit_price: float):
    alpaca_api.submit_order(LimitOrderRequest(
        symbol = pair,
        side = OrderSide.BUY,
        time_in_force = TimeInForce.GTC,
        notional = 50,
        stop_loss = settings.strats[pair]
    ))


'''
Market Order Sell Side
(Immediate Order)
'''
def sell_mo(pair: str):
    alpaca_api.submit_order(MarketOrderRequest(
        symbol=pair,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC,
        notional = 50,
        stop_loss = settings.strats[pair]['stop_loss']
    ))


'''
Limit Order Sell Side
(Preemptive)
'''
def sell_lo(pair: str, stop_price: float, stop_loss: float, limit_price: float):
    alpaca_api.submit_order(LimitOrderRequest(
        symbol=pair,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC,
        notional = 50,
        stop_loss = settings.strats[pair]['stop_loss'],
        limit_price = settings.strats[pair]['limit_price']
    ))


'''
Runs every <wait time> (should be at least 15 seconds by default) due to all of the free api limitations
'''
def update(pair: str, indicator: str):
    if not indicators.functions.get(indicator):
        print(f'Cannot find function for {indicator}')

    result = indicators.functions[indicator](pair)
    print(f'According to {indicator} we should place a {result} order on {pair}!')
