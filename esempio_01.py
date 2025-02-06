i = 0
countZero = 0
somma = 0
while True :
    numero = float (input())
    if numero == 0 :
        countZero += 1
        numero = float (input())
        if numero == 0 :
            countZero += 1
        if countZero == 2:
            break
        else:
            countZero = 0

    somma += numero

print ("La somma dei numeri inseriti è:", somma)