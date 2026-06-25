import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    return (
        salary.sort_values('salary', ascending = False)
        .drop_duplicates(subset='emp_id', keep='first')
        .sort_values('emp_id')
    )[['emp_id', 'firstname', 'lastname', 'salary', 'department_id']]
