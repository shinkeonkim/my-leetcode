import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    statistics = employees.groupby('dep_id', as_index=False)['emp_id'].count().rename(columns={'emp_id': 'count'})
    statistics = statistics[statistics['count'] == statistics['count'].max()]

    return statistics.merge(
        employees[employees['position'] == 'Manager'],
        on='dep_id'
    ).rename(columns={'emp_name': 'manager_name'})[['manager_name', 'dep_id']]
