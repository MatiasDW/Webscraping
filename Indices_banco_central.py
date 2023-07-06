import requests
from bs4 import BeautifulSoup as b

url = 'https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx'

html = requests.get(url)
content = html.content
soup = b(content,"lxml")


Uf = soup.find("label",{"id":"lblValor1_1"})
Dolar = soup.find("label",{"id":"lblValor1_3"})
Euro = soup.find("label",{"id":"lblValor1_5"})
Oro = soup.find("label",{"id":"lblValor2_3"})
Plata = soup.find("label",{"id":"lblValor2_4"})
Cobre = soup.find("label",{"id":"lblValor2_5"})

print(Uf,"UF")
print(Dolar,"USD")
print(Euro,"EUR")
print(Oro,"Oro")
print(Plata,"Plata")
print(Cobre,"Cobre")