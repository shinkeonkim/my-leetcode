import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    weekend = (tasks['submit_date'].dt.weekday >= 5).sum()
    working = (tasks['submit_date'].dt.weekday < 5).sum()

    return pd.DataFrame({ 'weekend_cnt' : [weekend], 'working_cnt': [working]})


    