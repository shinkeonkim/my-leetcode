import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    salaries = salaries.merge(
        salaries.groupby('company_id')['salary'].max().reset_index(name='max_salary'),
        on='company_id'
    )

    salaries['tax_rate'] = 49
    salaries.loc[salaries['max_salary'] <= 10000, 'tax_rate'] = 24
    salaries.loc[salaries['max_salary'] < 1000, 'tax_rate'] = 0
    
    salaries['salary'] = ((salaries['salary'] * (100 - salaries['tax_rate']) + 50) // 100).astype(int)

    return salaries[['company_id', 'employee_id', 'employee_name', 'salary']]

    
