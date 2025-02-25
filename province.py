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
province = pd.DataFrame (columns=["sigla","nome","abitanti"])
#aggiungere alla estrazione il numero di abitanti
#salvare il contenuto con pickle nel file di nome province ordinato per numero di abitanti decrescente

riga = riga.find_next("tr")
i=0
while riga != None:
    tdx = riga.find_next("td")
    tdx = tdx.find_next("td")
    provincia = tdx.get_text()
    #print(provincia)
    tdx = tdx.find_next("td") 
    residenti_txt = tdx.get_text()  #leggiamo il numero in formato 1.260.142
    residenti_txt = residenti_txt.replace('.', '')
    try:
        residenti = int(residenti_txt)
    except ValueError:
        print("The retrieved text is not a valid integer.")
        residenti = 0  # or some default value
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    sigla = tdx.get_text()
    province.loc[i]=[sigla,provincia,residenti]
    if sigla == "VT" : break
    i += 1
    riga = riga.find_next("tr")

print(province)
province_sorted = province.sort_values(by="abitanti", ascending=False)
print(province_sorted)

import pickle
dbfile = open('province','wb') #creare un file
pickle.dump(province_sorted,dbfile)
dbfile.close()
