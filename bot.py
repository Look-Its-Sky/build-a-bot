import indicators as indicators, settings  
import json, datetime

'''
Runs every <wait time> (should be at least 15 seconds by default) due to all of the free api limitations
'''
def update(pair: str, indicator: str):
    if not indicators.functions.get(indicator):
        print(f'Cannot find function for {indicator}')

    result = indicators.functions[indicator](pair)
    print(f'{datetime.now().strftime("[%D @ %H:%M:%S]")}: According to {indicator} we should {result} on {pair}!')
