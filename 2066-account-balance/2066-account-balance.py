import pandas as pd

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['balance'] = transactions['amount'] * transactions['type'].map({ 'Deposit': 1, 'Withdraw': -1})

    transactions = transactions.groupby(['account_id', 'day'], as_index=False).sum().sort_values(['account_id', 'day'], ascending=[True, True])

    transactions['balance'] = transactions.groupby(['account_id'], as_index=False)['balance'].cumsum()

    return transactions[['account_id', 'day', 'balance']]
