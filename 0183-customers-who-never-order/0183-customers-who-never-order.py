import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')

    merged = merged[merged['customerId'].isnull()].rename(columns={'name': 'Customers'})

    return merged[['Customers']]