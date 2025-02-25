import urllib.request
address = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(address)
theBytes = response.read()
#print(response)
#print(dir(response))
#print (theBytes)
html = theBytes.decode(encoding='iso-8859-1')
from bs4 import BeautifulSoup
doc = BeautifulSoup(html,"html.parser")
#print(doc.prettify())
t1 = doc.table
t2=t1.find_next("table")
t3=t2.find_next("table")
t4 =t3.find_next("table")
#print(t4)
riga = t4.find_next("tr")

import pandas as pd
province = pd.DataFrame (columns=["sigla","nome"])

riga = riga.find_next("tr")
i=0
while riga != None:
    tdx = riga.find_next("td")
    tdx = tdx.find_next("td")
    provincia = tdx.get_text()
    print(provincia)
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    sigla = tdx.get_text()
    province.loc[i]=[sigla,provincia]
    if sigla == "VT" : break
    i += 1
    riga = riga.find_next("tr")

print(province)
    
print (province[(province.sigla >= "P")& (province.sigla <= "PZ")])