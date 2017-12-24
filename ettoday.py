import requests
ettoday = requests.get('https://www.ettoday.net/news/news-list.htm')
from bs4 import BeautifulSoup
soup = BeautifulSoup(ettoday.text, 'html.parser')
data = soup.select('.part_list_2 h3')
for articles in data:
    tag = articles.find('em', 'tag').text
    time = articles.find('span', 'date').text
    url = articles.find('a').get('href')
    title = articles.find('a').text
    print(tag, time, url, title)
