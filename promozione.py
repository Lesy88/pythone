"realizzate una classe Cliente che gestisca le informazioni relative ad un Cliente di una campagna di promozione commerciale sotto forma di premi fedeltà. Dopo aver effettuato acquisti per almeno 100 euro il cliente riceve uno sconto di 10 euro sul sucessivo acquisto. Progettate queste metodi: effetuaAcquisto (self,ammontare) - registra un (nuovo) acquisto e accumula  , scontoRAggiounto(self)- deve restitueire true se sconto è attivo e subito lo annulla. "
class Cliente:
    def __init__(self, nome):
        self.nome = nome  # Nome del cliente
        self.acquisti_totali = 0  # Totale degli acquisti fatti
        self.sconto_attivo = False  # Flag che indica se lo sconto è attivo

    def effettuaAcquisto(self, ammontare):
        """Registra un nuovo acquisto e accumula l'importo totale degli acquisti."""
        if self.sconto_attivo:
            if ammontare >= 10 :
                ammontare -= 10  # Applica lo sconto di 10 euro
                self.acquisti_totali = 0  # Totale degli acquisti fatti
                
            else :
                ammontare = 0
                self.acquisti_totali = 0  # Totale degli acquisti fatti
                
            self.sconto_attivo = False  # Annulla lo sconto dopo l'utilizzo
        
        self.acquisti_totali += ammontare  # Aggiungi l'ammontare all'acquisto totale

        # Verifica se l'importo totale degli acquisti è almeno 100 euro
        if self.acquisti_totali >= 100:
            self.sconto_attivo = True  # Attiva lo sconto di 10 euro per il prossimo acquisto
           

    def scontoAggiunto(self):
        """Restituisce True se lo sconto è attivo e lo annulla."""
        if  self.sconto_attivo:
            self.sconto_attivo = False
            return True
        return False  # Se lo sconto non è attivo, restituisce False
    
    def __repr__(self):
        """Restituisce una stringa di rappresentazione del cliente."""
        return f"Cliente {self.nome}, Totale Acquisti: {self.acquisti_totali}€, Sconto Attivo: {self.sconto_attivo}"

# Esempio di utilizzo
cliente = Cliente("Mario Rossi")

# Effettua alcuni acquisti
cliente.effettuaAcquisto(40) 
print(cliente)  
cliente.effettuaAcquisto(60) 
print(cliente)
# Cliente effettua un acquisto con sconto
cliente.effettuaAcquisto(5)
print(cliente)
cliente.effettuaAcquisto(50)
print(cliente)
cliente.effettuaAcquisto(60)
print(cliente)
cliente.effettuaAcquisto(20)
print(cliente)
