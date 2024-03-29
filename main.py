import time
import settings, bot, indicators

if __name__ == "__main__":
    print("Started Trading Bot!")
    while True:
        for p in settings.strats.keys():
            for i in settings.indicators:
                bot.update(pair=p, indicator=i)
            
            #calc the play
            longest = indicators.results['buy']
            result = ''
            if indicators.results['sell'] == indicators.results['buy'] == indicators.results['hold'] or indicators.results['hold'] > indicators.results['sell'] and indicators.results['hold'] > indicators.results['buy']:
                result = 'hold'

            if indicators.results['sell'] > indicators.results['buy'] and indicators.results['sell'] > indicators.results['hold']:
                result = 'sell'

            if indicators.results['buy'] > indicators.results['sell'] and indicators.results['sell'] > indicators.results['hold']:
                result = 'buy'

            #play time
            if result == 'buy':
                bot.buy_mo(p) 
            
            if result == 'sell' and len(bot.alpaca_api.get_all_positions()) != 0:
                bot.sell_mo(p)
            
            results = {
                'buy': [],
                'sell': [],
                'hold': []
            }
