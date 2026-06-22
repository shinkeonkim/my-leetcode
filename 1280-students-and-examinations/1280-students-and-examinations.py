import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_cases = pd.merge(students, subjects, how='cross')

    counting = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    counting_cases = pd.merge(
        all_cases,
        counting,
        left_on = ['student_id', 'subject_name'],
        right_on = ['student_id', 'subject_name'],
        how='outer'
    )

    counting_cases['attended_exams'] = counting_cases['attended_exams'].fillna(0).astype(int)

    return counting_cases

    