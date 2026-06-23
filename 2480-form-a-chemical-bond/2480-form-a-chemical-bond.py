import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(
        elements[elements['type'] == 'Metal'][['symbol']].rename(columns={'symbol': 'metal'}),
        elements[elements['type'] == 'Nonmetal'][['symbol']].rename(columns={'symbol': 'nonmetal'}),
        how='cross'
    )