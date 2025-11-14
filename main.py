
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://ads.vk.com/cases'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all(class_="case-card_wrapper__F9fy_")

cases_massive = []

for card in cards:
    a = dict()
    relative_link = card.get("href")   
    title = card.get_text(strip=True)   
    true_link = urljoin(url, relative_link)
    a = {'Название кейса': title[10:] , 'Дата публикации': title[:10 ] , 'Ссылка': true_link}
    cases_massive.append(a)

for i, case in enumerate(cases_massive, start=1):
    print(f"Кейс №{i}")
    print(f"Название: {case['Название кейса']}")
    print(f"Дата: {case['Дата публикации']}")
    print(f"Ссылка: {case['Ссылка']}")
    print("_" * 40)
