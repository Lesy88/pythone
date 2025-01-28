numero = input ('Inserire i voti da 1 fino 10:')
contatore = 0
sommaParziale = 0
votiCinema = []

def isNumero(stringaNumero):
    if len(stringaNumero)>0:
        if stringaNumero.isdigit() :
            return True
        else:
            if stringaNumero.startswith('-') and stringaNumero[1:].isdigit():
                return True
            else: 
                return False
    else :
        return False
if not isNumero(numero) :
    print ("Fornire almeno un numero")
    exit()
    
while isNumero(numero) :
    contatore += 1
    votiCinema.append(int(numero))
    numero = input ("Inserci il prossimo voto:  \n")

for numero in votiCinema :
    if numero == min(votiCinema):
       votiCinema.remove(numero)
       break
   
print(votiCinema)
print("La media dei voti è", sum(votiCinema)/len(votiCinema))