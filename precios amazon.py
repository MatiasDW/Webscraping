import requests 
import openpyxl
from bs4 import BeautifulSoup as b 

#workbook = openpyxl.Workbook('Amazon.xlsx')
#worksheet = workbook.add_worksheet()
#worksheet.write('A1','Producto')
#worksheet.write('B1','Precio')

url = 'https://www.amazon.com/s?k=apple&crid=2IL5NCCZAVSMD&sprefix=apple%2Caps%2C266&ref=nb_sb_noss_1'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Ecoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT":"1"
    }
html = requests.get(url,headers=headers)
content = html.content
soup = b(content,"lxml")
print(soup)
row = 1
for post in soup.findAll("div",{"a-section a-spacing-small a-spacing-top-small"}):
    titulo = post.find("span",{"a-size-medium a-color-base a-text-normal"})
    precio = post.find("span",{"class":"a-offscreen"})
    if precio is not None:
        print(titulo)
        print(precio)
        #worksheet.write(row,0,titulo)
        #worksheet.write(row,1,precio)
        #row += 1
#workbook.close()