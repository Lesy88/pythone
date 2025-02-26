CONTINUARE = True
import os
import sys
# Creare una lista vuota
lista = []
nome=input("Inserire il nome del file TXT: ")
if not os.path.exists(nome):
    print ("Il file non esiste")
    sys.exit()

# Lettura del file di testo con la chiusura automatica
with open(nome, mode="r") as fh:
    while CONTINUARE :
        for riga in fh:
            if riga == "NO":
                CONTINUARE = False
            else:
            # Invertire la riga e aggiungerla alla lista
                riga_invertita = riga[::-1]
                lista.append(riga_invertita)

print("La lista invertita è:", lista)