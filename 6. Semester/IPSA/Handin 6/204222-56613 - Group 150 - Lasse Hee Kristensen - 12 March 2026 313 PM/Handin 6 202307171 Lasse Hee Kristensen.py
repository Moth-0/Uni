#%%
'''
Vi bruger keywords i constructoren til at sørge for default værdierne af alle objekters attributes er None.

Min metode str sørger for at returnere navnet op ibjektet og fødsel til dødsdato. AnnotatedPerson er
en subclass af person og i constructoren tilføjer vi en "note", men arver resten fra Person.
Det samme med __string__ som lige skal appende den note, AppendedPerson kan have som argument.
Havde flest problemere med ancestors funktionen som jo skal lede efter ancestors rekursivt, dvs
kalde sig selv når den returnerer en tuple med str, men kun hvis der eksisterer en mor/far i objektet.


'''

class Person():
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
            self.name = name
            self.mother = mother
            self.father = father
            self.born = born
            self.died = died

    def __str__(self):
        name_string = f"{self.name}, {self.born} - {self.died}, "
        return name_string
    
    def ancestors(self):
            
            father_ancestors = self.father.ancestors() if self.father else "-"
            mother_ancestors = self.mother.ancestors() if self.mother else "-"
            
            return(self.__str__(), father_ancestors, mother_ancestors)
    
class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note = ""):
            self.note = note
            super().__init__(name, mother, father, born, died)
        
    def __str__(self, ):
        return super().__str__() + self.note
    
louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

margrethe_ii.ancestors()

# %%
