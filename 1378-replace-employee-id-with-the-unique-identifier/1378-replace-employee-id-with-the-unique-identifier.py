import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    joined = employees.set_index('id').join(employee_uni.set_index('id'), how='left')

    return joined
