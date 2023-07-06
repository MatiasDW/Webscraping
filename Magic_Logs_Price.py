import requests
from bs4 import BeautifulSoup as b

url = 'https://oldschool.runescape.wiki/w/Magic_logs'


html = requests.get(url)
content = html.content
soup = b(content,"lxml")

Magic = soup.find("span",{"class":"infobox-quantity-replace"})


print(Magic,"Precio Magic logs GE")

