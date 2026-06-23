import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    a = school_a[['student_id', 'student_name']].rename(columns={'student_name': 'member_A', 'student_id': 'id_A'})
    b = school_b[['student_id', 'student_name']].rename(columns={'student_name': 'member_B', 'student_id': 'id_B'})
    c = school_c[['student_id', 'student_name']].rename(columns={'student_name': 'member_C', 'student_id': 'id_C'})

    merged = a.merge(b, how='cross').merge(c, how='cross')

    return merged[
        (merged['member_A'] != merged['member_B']) & 
        (merged['member_A'] != merged['member_C']) & 
        (merged['member_B'] != merged['member_C']) &
        (merged['id_A'] != merged['id_B']) & 
        (merged['id_A'] != merged['id_C']) & 
        (merged['id_B'] != merged['id_C'])
    ][['member_A', 'member_B', 'member_C']]
