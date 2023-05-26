import time
import settings, bot

if __name__ == "__main__":
    while True:
        for p in settings.strats.keys():
            for i in settings.indicators:
                bot.update(pair=p, indicator=i)
                time.sleep(5) #should at least be 4? seconds assuming all APIs are free tier