from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen("http()://www.pythonscraping,com/page5;/pag23.html")

soup = 85(html, 'html.paraser')
print(soup)

for sibling in soup.find("table",{"id": "giftList"}).tr.nect+sibling:
    print(sibling)


soup.find_all()
