import pandas as pd

# Загрузка данных из файла
train_data = pd.read_csv('data/train.csv')

# Удаление дубликатов
train_data = train_data.drop_duplicates()

# Перезапись файла с новыми данными
train_data.to_csv('data/train.csv', index=False)