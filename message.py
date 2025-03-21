"""Realizzare una classe Message, che rappresenti un modello per messaggi di posta elettronica. 
Un messaggio ha:
- un destinatario, 
- un mittente e 
- un testo. 
Progettate i metodi seguenti: un costruttore che riceve il mittente e il destinatario,
il metodo append che aggiunge una riga in fondo al testo del messaggio
il metodo to toString ce trasforma il messaggio in un'unica lunga stringa.
Scrivete un programma che usi questa classe per creare un messaggio e visualizzarlo.
"""
class Message :
    def __init__(self, destinatario, mittente) : #costruttore della classe
        self._destinatario = destinatario #qualifichiamo le variabili della cLasse
        self._mittente = mittente
        self._corpoMessaggio = []
        #print(type(self._corpoMessaggio))

    def append(self, riga):
        self._corpoMessaggio.append(riga)

    """def __str__(self):
        messaggio_completo = "Destinatario: " + self._destinatario + "\nMittente: " + self._mittente + "\n"
        #print(type(messaggio_completo))
        messaggio_completo += '\n'.join(self._corpoMessaggio)  # Unisce la stringa con la lista
        #print(type(messaggio_completo))
        return messaggio_completo"""
    def toString(self):
        messaggio_completo = "Destinatario: " + self._destinatario + "\nMittente: " + self._mittente + "\n"
        #print(type(messaggio_completo))
        messaggio_completo += '\n'.join(self._corpoMessaggio)  # Unisce la stringa con la lista
        #print(type(messaggio_completo))
        return messaggio_completo

# Creazione del messaggio
message = Message("mario@gmail.com", "luigi@posta.com")

# Aggiungiamo un'altra riga
message.append("Spero tu stia bene.")
message.append("Domani vengo a trovarti.")

# Visualizzazione del messaggio completo
print(message.toString())