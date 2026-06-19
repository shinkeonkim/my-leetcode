import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    sell_counts = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x : ','.join(sorted(x.unique())))
    ).reset_index()

    sell_counts = sell_counts.sort_values('sell_date')

    return sell_counts[['sell_date', 'num_sold', 'products']]

    
