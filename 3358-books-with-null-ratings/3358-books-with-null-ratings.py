import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    return books[books['rating'].isnull()][['book_id', 'title', 'author', 'published_year']].sort_values('book_id')