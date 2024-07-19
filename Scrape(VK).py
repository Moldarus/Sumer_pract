import vk_api
import pandas as pd

# Укажите ваш access token
access_token = ''

# Создаем сессию и авторизуемся
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

# Укажите ID или короткое имя группы
group_id = 'rut.digital'

# Получаем ID группы
group_info = vk.groups.getById(group_id=group_id)[0]
owner_id = -group_info['id']

# Задаем параметры запроса
count = 200  # Количество постов для получения за один запрос (максимум 100)
offset = 0
all_posts = []

while True:
    # Выполняем запрос к API для получения постов
    response = vk.wall.get(owner_id=owner_id, count=count, offset=offset)
    posts = response['items']

    if not posts:
        break

    all_posts.extend(posts)
    offset += count

# Создаем список для хранения данных о постах
posts_data = []

for post in all_posts:
    post_text = post.get('text', '')
    post_url = f"https://vk.com/wall{post['owner_id']}_{post['id']}"
    posts_data.append({'text': post_text, 'url': post_url})

# Сохраняем данные в DataFrame
df = pd.DataFrame(posts_data)

# Сохраняем результаты в CSV-файл
df.to_csv('vk_posts.csv', index=False)
