import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    try:
        salary = employee['salary'].drop_duplicates().sort_values(ascending=False).iloc[N - 1] if N > 0 else None
    except:
        salary = None
    
    return pd.DataFrame({
        f'getNthHighestSalary({N})': [salary]
    })
    
