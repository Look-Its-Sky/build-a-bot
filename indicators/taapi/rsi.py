'''
RSI Indicator
'''
def rsi(pair: str) -> int:
    d = get_method_values(ticker=pair.split("/")[0], method='rsi')
    
    if not d.get('value'):
        return None #API error
    
    return d.get('value')
