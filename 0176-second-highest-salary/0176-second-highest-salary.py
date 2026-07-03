import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = sorted(employee['salary'].unique().tolist())

    print(salary)

    if len(salary) < 2:
        return pd.DataFrame({ 'SecondHighestSalary': [None] })
    
    return pd.DataFrame({ 'SecondHighestSalary': [salary[-2]] })
