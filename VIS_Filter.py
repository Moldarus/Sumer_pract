import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_excel('VIS.xlsx')

print(data)

df = pd.read_excel('list.xlsx')

print(df)


df1 = data.rename(columns={'ФИО студента': 'ФИО'})
df2 = df.rename(columns={'Фамилия имя отчество': 'ФИО'})

df = pd.merge(df1, df2[['ФИО', 'Дата рождения', 'Тип']], on='ФИО', how='left')

df['Позиция в рейтинге'] = df['Позиция в рейтинге'].fillna(0).astype(int)

df.to_excel('result.xlsx', index=False)

df = pd.read_excel('result.xlsx')

print(df.dropna(subset=["Дата рождения"]))

