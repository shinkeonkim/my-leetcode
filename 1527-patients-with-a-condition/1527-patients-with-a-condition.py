import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    cond = patients['conditions'].apply(lambda x : any(word.startswith("DIAB1") for word in str(x).split()))

    return patients[cond]