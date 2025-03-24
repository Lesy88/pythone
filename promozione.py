
class Cliente:
    def __init__(self, nome):
        self._nome = nome  # Nome del cliente
        self._acquisti_totali = 0  # Totale degli acquisti fatti
        self._sconto_attivo = False  # Flag che indica se lo sconto è attivo

    def effettuaAcquisto(self, ammontare):
        """Registra un nuovo acquisto e accumula l'importo totale degli acquisti."""
        
        # Chiama il metodo scontoRaggiunto per verificare se lo sconto è attivo e applicarlo
        if self.scontoRaggiunto():
            if ammontare >= 10:
                ammontare -= 10  # Applica lo sconto di 10 euro
            else:
                ammontare = 0  # Se l'acquisto è inferiore a 10, azzera l'importo
        
        self._acquisti_totali += ammontare  # Aggiungi l'ammontare all'acquisto totale

        # Verifica se l'importo totale degli acquisti è almeno 100 euro
        if self._acquisti_totali >= 100 and not self._sconto_attivo:
            self._sconto_attivo = True  # Attiva lo sconto di 10 euro per il prossimo acquisto

    def scontoRaggiunto(self):
        """Restituisce True se lo sconto è attivo e lo annulla."""
        if self._sconto_attivo:
            self._sconto_attivo = False  # Annulla lo sconto dopo l'applicazione
            return True  # Lo sconto è stato applicato
        return False  # Lo sconto non è attivo, quindi non viene applicato

    def __repr__(self):
        """Restituisce una stringa di rappresentazione del cliente."""
        return f"Cliente {self._nome}, Totale Acquisti: {self._acquisti_totali}€, Sconto Attivo: {self._sconto_attivo}"

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
