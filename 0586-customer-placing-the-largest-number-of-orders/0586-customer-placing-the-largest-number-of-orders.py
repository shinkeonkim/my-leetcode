import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    max_order = orders.groupby('customer_number')['order_number'].nunique().max()

    return (
        orders.groupby('customer_number', as_index=False)['order_number']
        .nunique()
        .query('order_number == @max_order')
        [['customer_number']]
    )
