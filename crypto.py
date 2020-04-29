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

print(crypto[0])
print(fin[0][3:7])




# JPY = str(cry[0] + 'RUB')
# USD = str('USD -' + cur[1] + 'RUB')
# EURO = str('EURO -' + cur[2] + 'RUB')

# currency = currency.text
# print(currency)

#
# def jpy():
#     return JPY
#
#
# def usd():
#     return USD
#
#
# def euro():
#     return EURO
