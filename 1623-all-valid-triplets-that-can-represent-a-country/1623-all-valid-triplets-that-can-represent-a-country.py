import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    condition = '(student_name_a != student_name_b) & (student_name_a != student_name) & (student_name_b != student_name) & ' + \
        '(student_id_a != student_id_b) & (student_id_a != student_id) & (student_id_b != student_id)'
    return school_a.merge(
        school_b,
        how='cross',
        suffixes=('_a', '_b')
    ).merge(
        school_c,
        how='cross',
    ).query(condition).rename(
        columns={
            'student_name_a': 'member_A',
            'student_name_b': 'member_B',
            'student_name': 'member_C'
        }
    )[['member_A', 'member_B', 'member_C']]
