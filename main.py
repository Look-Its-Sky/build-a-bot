import time
import settings, bot, indicators

if __name__ == "__main__":
    print("Started Trading Bot!")

    strategy = eval(f"strategy.{settings.keys['strategy']}") # kind of dangerous lets come up with something else next tie
    
    while True:
        # get indicator values ready
        strategy.needed_indicators


        print(f'{datetime.now().strftime("[%D @ %H:%M:%S]")}: According to {indicator} we should {result} on {pair}!')
