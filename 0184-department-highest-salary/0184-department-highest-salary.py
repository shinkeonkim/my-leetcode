import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        department, 
        left_on='departmentId', 
        right_on='id',
        suffixes=('_emp', '_dept')
    )

    merged['ranking'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)

    result = merged[merged['ranking'] == 1]

    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result