'''
HANDIN 6 (ancestors)

This handin is done by (study ids and names of up to three students):

    202407458 Kenny Nguyen
    202408911 Safiya Chebil 
    202406237 Marie Schnoor - Madsen 
    
Reflection upon solution:

    rekursion var det vanskeligste å forstå, men det blev lettere når vi så på det i klassen og fik forklart det. 
    Det var også vanskelig å forstå hvordan man skulle bruge rekursion i denne oppgave.
'''





#Exercise 12.2 - handin 6 (ancestors)
class  Person:
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
        
    def __str__(self):
        return f'{self.name} {self.born}-{self.died}'

    def ancestors(self): 
        far = self.father.ancestors() if self.father is not None else '-'
        mor = self.mother.ancestors() if self.mother is not None else '-'
        return (str(self), far, mor)

    
    def recursive_method(self,L, prefix):
        print(prefix + f'--{L[0]}')
        
        prefix += '  |' #hver gang vi går dypere ligger vi en prefix til prefix
        for child in L[1:]:
            self.recursive_method(child,prefix)


class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        super().__init__(name, mother, father, born, died)
        self.note = note
    def __str__(self):
        basis = super().__str__()
        return f'{basis} [{self.note}]'

louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

L = margrethe_ii.ancestors()
margrethe_ii.recursive_method(L,'')