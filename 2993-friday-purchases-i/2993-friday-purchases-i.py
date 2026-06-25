import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases = purchases[purchases['purchase_date'].dt.weekday == 4]

    ans = purchases.groupby('purchase_date', as_index=False)['amount_spend'].sum()
    ans = ans.rename(columns={'amount_spend': 'total_amount'})
    ans['week_of_month'] = (ans['purchase_date'].dt.day - 1) // 7 + 1

    return ans[['week_of_month', 'purchase_date', 'total_amount']]