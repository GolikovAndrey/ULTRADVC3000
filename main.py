import pandas as pd

# Загрузка данных из файла
train_data = pd.read_csv('data/train.csv')

print(train_data.head())

# Удаление дубликатов
train_data = train_data.drop_duplicates()

print(train_data.shape)

train_data = train_data[["Pclass", "Sex", "Age"]]

print(train_data.shape)
print(train_data.head())

# Перезапись файла с новыми данными
train_data.to_csv('data/train.csv', index=False)