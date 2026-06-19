import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users = users[users['mail'].str.match(r'[a-zA-Z][0-9a-zA-Z_\.\-]*@leetcode\.com$')]

    return users