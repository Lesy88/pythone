fineGioco = False
puntiGiocatore1 = 0
puntiGiocatore2 = 0
while not fineGioco:
    numeroGiocatore = int(input("1 or 2"))
    print(numeroGiocatore)
    if numeroGiocatore == 1:
        puntiGiocatore1 += 1
        print(puntiGiocatore1,puntiGiocatore2)
    else:
        puntiGiocatore2 += 1
        print(puntiGiocatore1,puntiGiocatore2)
    if (puntiGiocatore2 == 4 or puntiGiocatore1 == 4):
        fineGioco = True
print(puntiGiocatore1,puntiGiocatore2)