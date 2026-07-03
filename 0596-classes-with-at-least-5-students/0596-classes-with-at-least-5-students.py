import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses.groupby('class', as_index=False)['student']
            .nunique()
            .query('student >= 5')[['class']]
    )