import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

def round_half_up(val, decimals=2):
    if pd.isna(val):
        return val

    path = f".{'0' * decimals}" if decimals > 0 else '1'
    return float(Decimal(str(val)).quantize(Decimal(path), rounding=ROUND_HALF_UP))


def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    trial_users = set(user_activity[user_activity['activity_type'] == 'free_trial']['user_id'])
    paid_users = set(user_activity[user_activity['activity_type'] == 'paid']['user_id'])
    converted_users = trial_users & paid_users

    result = (
        user_activity[user_activity['user_id'].isin(converted_users)]
        .pivot_table(index='user_id', columns='activity_type', values='activity_duration', aggfunc='mean')
        .reset_index()
    )

    result['free_trial'] = result['free_trial'].apply(lambda x: round_half_up(x, 2))
    result['paid'] = result['paid'].apply(lambda x: round_half_up(x, 2))
    
    return (
        result[['user_id', 'free_trial', 'paid']]
        .rename(columns={'free_trial': 'trial_avg_duration', 'paid': 'paid_avg_duration'})
        .sort_values('user_id')
    )
