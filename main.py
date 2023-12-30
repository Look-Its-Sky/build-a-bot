import time
import settings, bot, indicators
from strategies import test
from indicators import taapi

pair = 'ETHUSD'

if __name__ == "__main__":
    print("Started Trading Bot!")

    #strategy = eval(f"strategies.{settings.keys['strategy']}") # kind of dangerous lets come up with something else next tie

    strategy = test
    while True:
        test.update({
            'rsi': taapi.rsi.rsi(pair),
            'bbands2': taapi.bbands2.bbands2(pair)
        })
        print(f'{datetime.now().strftime("[%D @ %H:%M:%S]")}: According to {indicator} we should {result} ')#on {pair}!')

    
