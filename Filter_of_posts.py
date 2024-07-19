import pandas as pd

# Загрузка данных из файла vk_posts.csv
vk_posts_file = 'vk_posts.csv'  # Путь к файлу с данными постов VK
df_vk_posts = pd.read_csv(vk_posts_file)

# Загрузка данных из Excel
excel_file_path = 'result.xlsx'  # Укажите путь к вашему файлу Excel
sheet_name = 'Sheet1'  # Имя листа в файле Excel, из которого будем считывать данные
column_name = 'ФИО'  # Имя столбца с ФИО

df_excel = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Извлечение значений из столбца ФИО, исключая пустые значения
full_names = df_excel[column_name].dropna().tolist()

# Функция для извлечения фамилии из ФИО
def extract_last_name(full_name):
    if isinstance(full_name, str):
        parts = full_name.split()
        if len(parts) >= 1:
            return parts[0]  # Возвращаем только фамилию
    return None  # Если формат неправильный, возвращаем None

# Функция для фильтрации постов по фамилии
def filter_posts_by_last_name(posts_df, last_name):
    filtered_posts_df = posts_df[posts_df['text'].str.contains(last_name, case=False, na=False)]
    filtered_posts_df['ФИО студента'] = last_name
    filtered_posts_df = filtered_posts_df[['ФИО студента', 'text', 'url']]
    return filtered_posts_df

# Создание списка для хранения отфильтрованных постов
filtered_posts_data = pd.DataFrame(columns=['ФИО студента', 'text', 'url'])

# Фильтрация постов по каждому ФИО из Excel
for full_name in full_names:
    last_name = extract_last_name(full_name)
    if last_name:
        filtered_posts_df = filter_posts_by_last_name(df_vk_posts, last_name)
        filtered_posts_data = pd.concat([filtered_posts_data, filtered_posts_df])

# Сохранение результатов в CSV-файл
filtered_posts_data.to_csv('filtered_vk_posts.csv', index=False)
