from alpaca.trading.client import TradingClient
from alpaca.trading.requests import *
from alpaca.trading.enums import OrderSide, TimeInForce
import settings

alpaca_api = TradingClient(settings.keys['alpaca_api'], settings.keys['alpaca_secret'], paper=True)

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
