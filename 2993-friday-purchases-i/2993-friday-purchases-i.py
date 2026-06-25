import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    return (
        purchases[purchases['purchase_date'].dt.weekday == 4]
        .groupby('purchase_date', as_index=False)['amount_spend'].sum()
        .rename(columns={'amount_spend': 'total_amount'})
        .assign(week_of_month=lambda x: (x['purchase_date'].dt.day - 1) // 7 + 1)
        [['week_of_month', 'purchase_date', 'total_amount']]
    )