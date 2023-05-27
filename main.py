import time
import settings, bot, indicators

if __name__ == "__main__":
    while True:
        for p in settings.strats.keys():
            for i in settings.indicators:
                bot.update(pair=p, indicator=i)
                time.sleep(5) #should at least be 4? seconds assuming all APIs are free tier
            
            #calc the play
            longest = settings.indicators['buy']
            result = ''
            if settings.indicators['sell'] == settings.indicators['buy'] == settings.indicators['hold'] or settings.indicators['hold'] > settings.indicators['sell'] and settings.indicators['hold'] > settings.indicators['buy']:
                result = 'hold'

            if settings.indicators['sell'] > settings.indicators['buy'] and settings.indicators['sell'] > settings.indicators['hold']:
                result = 'sell'

            if settings.indicators['buy'] > settings.indicators['sell'] and settings.indicators['sell'] > settings.indicators['hold']:
                result = 'buy'

            #play time
            if result == 'buy':
                bot.buy_mo(p) 
            
            if result == 'sell' and len(bot.alpaca_api.get_all_positions()) != 0:
                bot.sell_mo(p)