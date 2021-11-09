import pandas as pd

df = pd.read_csv('input.csv')
df.columns = df.columns.str.replace(' ', '')

passing_grades = {(80, 100): 'A',
                  (70, 79.9): 'B',
                  (60, 69.9): 'C',
                  (50, 59.9): 'D',
                  (40, 49.9): 'E',
                  (0, 39.9): 'U'}


def grade_calc(x, b):
    return next((v for k, v in b.items() if k[0] <= x <= k[1]), None)


df['FinalMark'] = df['Algebra'] + df['Calculus'] + \
    df['Programming'] + df['Databases']
df.round(2)['AverageMark'] = df['FinalMark'] / 4
df['FinalGrade'] = df['AverageMark'].apply(
    grade_calc, b=passing_grades)

header = ["Firstname", "Surname", "AverageMark", "FinalGrade"]
df.to_csv('output.csv', columns=header)
