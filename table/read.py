import pandas as pd

df = pd.read_excel('')
df = df.rename(columns={'ФИО': 'name', 'Должность': 'staff'})
title = df.name
sum_men = len(list(df.name))

inf_1 = df[['name', 'height']]
pd.set_option('display.max_columns', None)

