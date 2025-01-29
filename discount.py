def discount(prices, isPet, nItems):
    i = 0
    discountAmount = 0
    amount = 0
    SCONTOFISSO = 0.2
    count_Y = isPet.count("Y")
    if count_Y >= 1:
        while prices[i] != -1 :
            if isPet[i] == "N":
                amount += nItems[i]
                i+=1
            else:
              i+=1
        if amount >= 5:
            i = 0        
            while prices[i] != -1 :
                if isPet[i] == "N":
                    discountAmount += prices[i]*nItems[i]*SCONTOFISSO
                    i+=1
                else:
                    i+=1
    return discountAmount
i = 0
prices = []
isPet = []
nItems = []

while True:
   price = float(input("Inserisci il prezzo: (-1 per la fine): "))
   prices.append(price) 
   if price == -1: 
      break
   isPet.append(input("è animale? (Y/N)"))
   nItems.append(int(input("Inserire la quantità:")))
   i += 1
   
print("\nPrezzi inseriti:", prices)
print("I prodotti:", isPet)
print("Quantita:",nItems)
print("Tuo sconto totale è ", discount(prices,isPet,nItems), "euro")
