import time
import settings, bot, indicators

if __name__ == "__main__":
    while True:
        for p in settings.strats.keys():
            for i in settings.indicators:
                bot.update(pair=p, indicator=i)
                time.sleep(30) #should at least be 4? seconds assuming all APIs are free tier
            
            longest = settings.indicators['buy']
            result = ''
            if settings.indicators['sell'] == settings.indicators['buy'] == settings.indicators['hold'] or settings.indicators['hold'] > settings.indicators['sell'] and settings.indicators['hold'] > settings.indicators['buy']:
                result = 'hold'

            if settings.indicators['sell'] > settings.indicators['buy'] and settings.indicators['sell'] > settings.indicators['hold']:
                result = 'sell'

            if settings.indicators['buy'] > settings.indicators['sell'] and settings.indicators['sell'] > settings.indicators['hold']:
                result = 'buy'