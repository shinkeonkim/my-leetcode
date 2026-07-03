import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return (
        actor_director.groupby(['actor_id', 'director_id'], as_index=False)
        ['timestamp'].nunique()
        .query('timestamp >= 3')
        [['actor_id', 'director_id']]
    )