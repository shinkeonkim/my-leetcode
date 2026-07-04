import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    reds = orders.merge(
        company,
        on='com_id'
    ).query("name == 'RED'")['sales_id'].tolist()

    return sales_person.query('sales_id not in @reds')[['name']]
