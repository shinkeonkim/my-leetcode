import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[products['name'].str.contains(r'(?<!\d)\d{3}(?!\d)', regex=True)]
