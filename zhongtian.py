import requests
zhongtian = requests.get('http://www.chinatimes.com/history-by-date/2017-12-24-2601?page=1')
from bs4 import BeautifulSoup
soup = BeautifulSoup(zhongtian.text, 'html.parser')
data = soup.select('.listRight ul li')
for articles in data:
    url = articles.find('a').get('href')
    title = articles.find('h2').text.strip()
    print(url, title)
