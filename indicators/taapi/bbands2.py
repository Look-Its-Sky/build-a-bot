'''
Bollinger Bands Indicator
'''
def bbands2(pair: str) -> tuple:
    d = get_method_values(pair=pair.split("/")[0], method='bbands2')
    if d == None or not d.get('valueUpperBand') or not d.get('valueLowerBand'):
        return None #API error couldnt get either band

    return d.get('valueLowerBand'), d.get('valueUpperBand')
