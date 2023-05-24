import indicators

orders = []

def buy(pair: str):
    pass

def sell(pair: str):
    pass

def update(pair: str, indicator: str):
    if not indicators.functions.get(indicator):
        print(f'Cannot find function for {indicator}')

    result = indicators.functions[indicator](pair)
    print(f'According to {indicator} we should {result}!')

    if result == 'buy':
        buy(pair)
