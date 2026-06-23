import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    return cities.groupby('state', as_index=False).agg({ 'city': lambda x : ', '.join(sorted(x))}).rename(columns={'city' : 'cities'})