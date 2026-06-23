import pandas as pd

def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # cta = pd.merge(
    #     salesperson,
    #     customer,
    #     left_on='salesperson_id',
    #     right_on='salesperson_id',
    #     how='left'
    # )

    cta = pd.merge(
        customer,
        sales,
        left_on='customer_id',
        right_on='customer_id'
    ).groupby('salesperson_id').agg(total=('price', 'sum')).reset_index()

    return pd.merge(
        salesperson,
        cta,
        left_on='salesperson_id',
        right_on='salesperson_id',
        how='left'
    ).fillna(0)
