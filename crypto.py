import requests
from bs4 import BeautifulSoup
import re

url = 'https://bitinfocharts.com/ru/markets/'

source = requests.get(url)
soup = BeautifulSoup(source.text, features="lxml")

# table = soup.findAll('table', {'class': 'cbr-kurs'})
cur = soup.findAll('tr', {'class': 'ptr'})
crypto = []
for i in cur:
    i = i.text
    crypto.append(i)

# print('\n'.join(crypto))

fin = []
for j in crypto:
    j = re.split(r'\W+', j)
    fin.append(j)

BTC = str('Стоимость ' + fin[0][3] + ' равна ' + fin[0][4] + fin[0][5] + '.' + fin[0][6] + ' USD')
ETH = str('Стоимость ' + fin[1][3] + ' равна ' + fin[1][4] + '.' + fin[1][5] + ' USD')
LTC = str('Стоимость ' + fin[2][3] + ' равна ' + fin[2][4] + '.' + fin[2][5] + ' USD')


def btc():
    return BTC


def eth():
    return ETH


def ltc():
    return LTC
