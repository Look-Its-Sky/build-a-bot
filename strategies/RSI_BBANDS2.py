class RSI_BBANDS_MA:
    needed_indicators = ['rsi', 'bbands']

    # settings
    rsi = {
        'upper': 65,
        'lower': 27
    }

    def __init__() -> None:
        pass

    def get_indicators() -> list:
        return tuple(indicators.keys())
    
    def update(indicators: dict) -> str:
        # indicators are the current values
        counter = {
            'hold': 0,
            'buy': 0,
            'sell': 0
        }
    
        # rsi
        if indicators['rsi'] > rsi['upper']:
            counter['sell'] += 1

        elif indicators['rsi'] < rsi['lower']:
            counter['buy'] += 1 

        else:
            counter['hold'] += 1

        # bbands
        if indicators['price'] > indicators['bbands_upper']:
            counter['sell'] += 1

        elif indicators['price'] < indicators['bbands_lower']:
            counter['buy'] += 1

        else:
            counter['hold'] += 1


        # calc votes
        sell_signal = counter['sell'] > counter['hold'] and counter['sell'] > counter['buy']
        buy_signal = counter['buy'] > counter['sell'] and counter['buy'] > counter['hold']

        if sell_signal:
            return 'sell'

        if buy_signal:
            return 'buy'

        return 'hold'
