import csv
import snscrape.modules.telegram as sntg

channel_names = []

# Открываем CSV-файл для записи
with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Записываем заголовок
    writer.writerow(['id', 'дата', 'текст поста'])

    # Извлекаем данные из каждого канала
    for channel_name in channel_names:
        scraper = sntg.TelegramChannelScraper(channel_name)
        for post in scraper.get_items():
            # Извлекаем id, дату и текст поста
            post_id = post.url
            post_date = post.date
            post_text = post.content

            # Записываем данные в CSV-файл
            writer.writerow([post_id, post_date, post_text])



