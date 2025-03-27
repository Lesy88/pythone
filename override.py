class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
    def __repr__(self):
        return self._nome+" "+self._cognome
    def __str__(self):
        return self._nome+" "+self._cognome


class Docente(Persona):
    def __init__(self, nome, cognome, materia) :
        super().__init__(nome,cognome)
        self._materia = materia

    def __str__(self):
        return self._nome +" "+self._cognome + " insegna: " + self._materia
    
class Studente(Persona):
    def __init__(self, nome, cognome, corso) :
        super().__init__(nome,cognome)
        self._corso = corso

    def __str__(self):
        return self._nome +" "+self._cognome + " frequenta il corso:" + self._corso

ar = Persona("Nome", "Cognome")
print(ar)
dc = Docente ("Roberto", "Rossi", "C++")
print(dc)
st = Studente ("Anna", "Ricci", "Cultura italiana")
print(st)
