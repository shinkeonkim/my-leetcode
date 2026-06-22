import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    candidates = candidates[candidates['years_of_exp'] >= 2] 
    scores = rounds.groupby('interview_id').agg(
        { 'score': 'sum' }

    )
    
    ans = candidates.merge(scores, left_on ='interview_id', right_on = 'interview_id')
    ans = ans[ans['score'] > 15][['candidate_id']]

    return ans