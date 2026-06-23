import numpy as np
import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['amount'] = stocks['price'] * stocks['operation'].map({'Buy': -1, 'Sell': 1})
    return stocks.groupby('stock_name')['amount'].sum().reset_index(name='capital_gain_loss')
