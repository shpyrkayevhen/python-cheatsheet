# Якщо website немає API єдиний шлях отримати з нього дані це парсити його html(tags)

# 1: pip install beautifulsoup4
#    pip install requests


from bs4 import BeautifulSoup
from pprint import pprint
import requests


url = 'https://stackoverflow.com/questions'
response = requests.get(url)


# 1 arg: передаємо HTML контент, який отримали з request
# 2 arg: тип парсера
soup = BeautifulSoup(response.text, 'html.parser')


#  -> return list елементи якого є екземплярами класу Tag
# Отримуємо дані з першої сторінки(паджинайшен). Можемо створити
# зовнішній цикл де перебиратимемо всі сторінки за такою ж логікою
# Знаходимо клас pagination і т.д.
questions = soup.select('.s-post-summary')
for question in questions:
    print(question.select_one('.s-link').get_text())
    print(question.select_one('.s-post-summary--stats-item-number').get_text())
