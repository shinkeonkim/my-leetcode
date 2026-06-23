import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    person['name'] = person['name'] + "(" + person['profession'].str[0:1] + ")"

    return person.sort_values('person_id', ascending=False)[['person_id', 'name']]