import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    items = purchases.merge(
        products,
        on='product_id'
    )
    
    items['price'] = items['price'] * items['quantity']

    max_invoice_id = (
        items
        .groupby('invoice_id')['price']
        .sum()
        .reset_index(name='price')
        .sort_values(['price', 'invoice_id'], ascending=[False, True])
    ).head(1).squeeze().to_dict()['invoice_id']

    return items[items['invoice_id'] == max_invoice_id][['product_id', 'quantity', 'price']]
