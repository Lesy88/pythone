riga= input("Inserisci per ezempio (3 A): ")
j = 1
pos = riga.find(" ")
if pos == -1:
    raise ValueError("Manca il separatore ")
righe=int(riga[: pos])
simbolo= riga[pos+1 : ]
spazio=righe
for i in range (0,righe) :
    print(" "*spazio,simbolo*j)
    j+=2
    spazio -= 1


