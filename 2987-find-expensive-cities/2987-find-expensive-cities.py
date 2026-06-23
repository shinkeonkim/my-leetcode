import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    grouping = listings.groupby('city', as_index=False).mean()
    return grouping[grouping['price'] > listings['price'].mean()][['city']]
