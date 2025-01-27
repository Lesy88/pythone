risposta = "no"
contatore = 0
somma_numeri = 0
while (risposta != 'fine') :
    numero_float = float(input ("metti numero:"))
    somma_numeri += numero_float
    contatore += 1 
    risposta = input ('fine?')
print ('La tua media è ', somma_numeri/contatore)


