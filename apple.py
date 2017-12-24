import requests
appleUrl = requests.get('https://tw.appledaily.com/new/realtime/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(appleUrl.text, 'html.parser')
data = soup.select('.rtddt')
for articles in data:
    url = articles.find('a').get('href')
    time = articles.find('time').text
    typee = articles.find('h2').text
    title = articles.find('h1').text
    print(title, url, typee)
