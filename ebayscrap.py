import requests
from bs4 import BeautifulSoup as b

url = 'https://www.ebay.com/globaldeals'

html = requests.get(url)
content = html.content
soup = b(content,"lxml")
#print(soup)

titulo_destacado = soup.find("h3",{"class":"dne-itemtile-title ellipse-3"})
precio_destacado = soup.find("span",{"itemprop":"price"})
print(titulo_destacado)
print(precio_destacado)