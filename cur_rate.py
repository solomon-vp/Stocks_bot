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


JPY = str(cur[0] + 'RUB')
USD = str('USD -' + cur[1] + 'RUB')
EURO = str('EURO -' + cur[2] + 'RUB')


# currency = currency.text
# print(currency)


def jpy():
    return JPY


def usd():
    return USD


def euro():
    return EURO
