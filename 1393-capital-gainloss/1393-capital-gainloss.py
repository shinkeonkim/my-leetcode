import numpy as np
import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['result_price'] = np.where(stocks['operation'] == 'Buy', -stocks['price'], stocks['price'])
    return stocks.groupby('stock_name').agg(capital_gain_loss=('result_price', 'sum')).reset_index()
