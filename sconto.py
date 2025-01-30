def discount(prices, isPet, nItems):
    i = 0
    discountAmount = 0
    amount = 0
    SCONTOFISSO = 0.2
    count_Y = isPet.count(True)
    if count_Y >= 1:
        while prices[i] != -1 :
            if isPet[i] == False:
                amount += 1
                i+=1
            else:
              i+=1
        if amount >= 5:
            i = 0        
            while prices[i] != -1 :
                if isPet[i] == False:
                    discountAmount += prices[i]*SCONTOFISSO
                    i+=1
                else:
                    i+=1
    return discountAmount
i = 0
prices = []
isPet = []
stringa = ""
while True:
   stringa = input("Inserisci il prezzo e codice (Y/N): (-1 per la fine): ")
   if stringa == "-1":
      prices.append(float(-1))
      break
   # Separiamo la stringa usando il metodo split()
   parte_numerica, parte_simbolica = stringa.split()
   # Converto la parte numerica in float
   price = float(parte_numerica)
   # La parte simbolica rimane come stringa
   codice = parte_simbolica
   prices.append(price) 
   if codice == "N":
     isPet.append(False)
   else:
      isPet.append(True)
   i += 1
print(prices)
print(isPet)
print("Tuo sconto totale è ", discount(prices,isPet,6), "euro")

