fineGioco = False
puntiGiocatore1 = 0
puntiGiocatore2 = 0
while not fineGioco:
    numeroGiocatore = int(input("metti numero di giocatore: 1 oppure 2 "))
    if numeroGiocatore == 1:
        puntiGiocatore1 += 1
    else:
        puntiGiocatore2 += 1
    if (puntiGiocatore1 == 4 and puntiGiocatore2 <= 2) or (puntiGiocatore1 >=6 and puntiGiocatore1-puntiGiocatore2>=2):
        print("Ha vinto giocatore 1")
        fineGioco = True
    if (puntiGiocatore2 == 4 and puntiGiocatore1 <= 2) or (puntiGiocatore2 >=6 and puntiGiocatore2-puntiGiocatore1>=2):
        print("Ha vinto giocatore 2")
        fineGioco = True
print(puntiGiocatore1,puntiGiocatore2)