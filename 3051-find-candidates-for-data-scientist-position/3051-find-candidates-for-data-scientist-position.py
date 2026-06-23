import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    return candidates[candidates['skill'] == 'Python'].merge(
        candidates[candidates['skill'] == 'Tableau'],
        on='candidate_id'
    ).merge(
        candidates[candidates['skill'] == 'PostgreSQL'],
        on='candidate_id'
    )[['candidate_id']].sort_values('candidate_id')
