'''''
This is done by :
748507 Kristian Milla

Reflection upon solution:
Rekursionsdelen blev overraskende intuitiv når den blev inkorporeret i klasserne.
Fik hjælp af AI med at super-funktionen, som gjorde det muligt at genbruge ting fra "moderklassen".
'''

class Person:
    def __init__(self, name = None, mother = None, father = None, born = None, died = None):
    #None: man kan oprette en person, selvom man ikke kender deres forældre endnu
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died

    def __str__(self):
        if self.died:
            dod = self.died
        else:
            dod = ""
        return f"{self.name} {self.born}-{dod}"
    
    def ancestors(self): 
        if self.father:
            f_anc = self.father.ancestors()
        else:
            f_anc = '-'
        
        if self.mother:
            m_anc = self.mother.ancestors()
        else:
            m_anc = '-'
        
        return (str(self), f_anc, m_anc)

class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        # super().__init__ kalder Person-klassens __init__
        super().__init__(name, mother, father, born, died)
        self.note = note

    def __str__(self):
        # Jeg genbruger Person's __str__ og tilføjer noten i [ ]
        basis_info = super().__str__()
        return f"{basis_info} [{self.note}]"
