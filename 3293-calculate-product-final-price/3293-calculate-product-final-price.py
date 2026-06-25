import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    ans = products.merge(
        discounts,
        on='category',
        how='left'
    ).sort_values('product_id').fillna(0)

    ans['final_price'] = ans['price'] * (100 - ans['discount']) / 100

    return ans[['product_id', 'final_price', 'category']]
