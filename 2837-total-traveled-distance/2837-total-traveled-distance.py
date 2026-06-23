import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return users.merge(
        rides,
        on='user_id',
        how='left'
    ).groupby(['user_id', 'name'], as_index=False)['distance'].sum().rename(columns={'distance': 'traveled distance'})