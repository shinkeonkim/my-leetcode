import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    new_york_count = len(new_york[new_york['score'] >= 90])
    california_count = len(california[california['score'] >= 90])

    print(new_york_count, california_count)

    winner = "New York University" if new_york_count > california_count else ("California University" if new_york_count < california_count else "No Winner")

    return pd.DataFrame({ "winner": [winner] })