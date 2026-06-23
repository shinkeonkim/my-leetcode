import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    avg = listings['price'].mean()
    return listings.groupby('city', as_index=False)['price'].mean().query('price > @avg')[['city']]