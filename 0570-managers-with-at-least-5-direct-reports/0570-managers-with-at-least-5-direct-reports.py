import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # employee.groupby('managerId')
    key_managers = employee.groupby('managerId') \
        .size() \
        .reset_index(name='team_members_count')
    
    key_managers = key_managers[key_managers['team_members_count'] >= 5]['managerId']

    ret = pd.merge(employee, key_managers, how='left', left_on='id', right_on='managerId')
    ret = ret[ret['managerId_y'].notnull()]
    return ret[['name']]

