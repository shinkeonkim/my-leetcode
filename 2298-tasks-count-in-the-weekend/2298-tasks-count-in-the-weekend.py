import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    is_weekend = tasks['submit_date'].dt.weekday >= 5

    return pd.DataFrame({
        'weekend_cnt': [is_weekend.sum()],
        'working_cnt': [(~is_weekend).sum()]
    })