import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['temp'] = delivery['order_date'] == delivery['customer_pref_delivery_date']
    return pd.DataFrame({'immediate_percentage': [(delivery['temp'].mean() * 100).round(2)]})
