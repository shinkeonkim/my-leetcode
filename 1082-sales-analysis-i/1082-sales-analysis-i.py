import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.groupby('seller_id')['price'].sum().reset_index(name='price')

    return sales[sales['price'] == sales['price'].max()][['seller_id']]
