class Employee:
    def __init__(self,nome,cognome) :
        self._nome = nome
        self._cognome = cognome
        self._salario = 0
    def setNome(self,nome):
        self._nome = nome
    def setCognome (self, cognome):
        self._cognome = cognome
    def setSalario (self, salario):
        self._salario = salario
    def __repr__(self):
        return self._nome +" "+self._cognome+ " con lo stipendio: " +str(self._salario)
    
class Manager(Employee):
    def __init__(self, nome, cognome, reparto) :
        super().__init__(nome,cognome)
        self._reparto = reparto

    def __repr__(self):
        return self._nome +" "+self._cognome+ " con lo stipendio: " +str(self._salario) + " gestisce il reparto: " + self._reparto

    
elena = Employee ("Elena", "Rossi")
elena.setSalario(1750)
print(elena)
dino = Manager ("Dino", "Mancini", "HR")
dino.setSalario (2500)
print(dino)