i = 0
countZero = 0
somma = 0
while True :
    stringa = input ("Inserisci il numero:")
    numero = float (stringa)
    if numero == 0 :
        countZero += 1
        stringa = input ("Inserisci il numero:")
        numero = float (stringa)
        if numero == 0 :
            countZero += 1
        if countZero == 2:
            break
        else:
            countZero = 0
            print ("countZero è:", countZero)

    somma += numero

print ("La somma dei numeri inseriti è:", somma)