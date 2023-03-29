
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError
import pandas as pd

result = []
for sido1 in range(1,18):
    sido2 = 1
    while(True):
        url = "https://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d" %(sido1,sido2)
        try:
            html = urllib.request.urlopen(url)
        except (HTTPError or URLError) as e:
            break
        print(url)
        soupChicken = BeautifulSoup(html, 'html.parser')
        tag_div = soupChicken.find('div', attrs={'class':'shopSchList'})
        for store in tag_div.find_all("span"):
            store_name = store.find('strong').string
            store_text = store.find('em').getText()
            store_data = store_text.strip().replace('\r',"").replace('\t',"").split("\n")
            store_sido = store_data[0].split(" ")[0]
            store_gungu = store_data[0].split(" ")[1]
            store_address = store_data[1].replace("(","").replace(")","")
            result.append([store_name]+[store_sido]+[store_gungu]+[store_address])
        sido2 += 1


kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'store_address'))
kyochon_tbl.to_csv("C:/Users/jin14/Desktop/kyochon.csv",encoding = "cp949", mode = "w", index = True)