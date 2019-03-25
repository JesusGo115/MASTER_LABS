from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

aSite = 'https://www.mysecretwoods.com/collections/our-rings'

requesting = Request( aSite, headers={'User-Agent': 'Mozilla/5.0'} )

returning = urlopen(requesting)

object1 = BeautifulSoup(returning.read(), 'lxml')

title = object1.body.h1
print(title.get_text())

for link in object1.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
