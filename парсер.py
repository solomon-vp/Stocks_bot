import requests
from bs4 import BeautifulSoup

url = 'http://banki.tomsk.ru/pages/41/'

source = requests.get(url)
soup = BeautifulSoup(source.text, features="lxml")

# table = soup.findAll('table', {'class': 'cbr-kurs'})
currency = soup.findAll('span', {'style': 'position: relative; bottom: 8px; left: 2px;'})
cur = []
for i in currency:
    i = i.text
    cur.append(i)

# currency = currency.text
print(currency)
print(cur)
