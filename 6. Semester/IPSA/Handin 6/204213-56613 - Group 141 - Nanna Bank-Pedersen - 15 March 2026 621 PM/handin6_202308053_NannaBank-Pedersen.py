'''
HANDIN 6 (ancestors)

This handin is done by:
    202308053 Nanna Bank-Pedersen

Reflection upon solution:
Jeg har brugt pythons funktion super() til at kalde metoder fra den overordnede klasse i underklassen.
Jeg havde problemer med at få det rigtige output med noten gennem annotated person, fordi jeg i starten 
bare havde return (self.name, father_anc, mother_anc)men så ændrede jeg det til return (str(self), m_anc, f_anc), 
så det inkluderede noten i str(self) og det virkede.
Det nemmere ved opgaven var at lave den rekursive struktur i ancestors metoden, hvor man bare kalder ancestors på 
både far og mor, og så returnere det som en tuple. Jeg antager at input er gyldige Person og AnnotatedPerson objekter, 
og har ikke lavet nogen begrænsninger på det i koden. 
Jeg er lidt i tvivl om hvordan rækkefølgen af name, far og mor i definitionen af klasserne skal være, måske du kan 
forklare det for mig i feedbacken?
'''
class Person:
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died

    def __str__(self):
        return f"{self.name} {self.born}-{self.died}"
    
    def ancestors(self):
        m_anc = self.mother.ancestors() if self.mother else '-'
        f_anc = self.father.ancestors() if self.father else '-'
        return (str(self), f_anc, m_anc)
  
class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        super().__init__(name, mother, father, born, died)
        self.note = note

    def __str__(self):
        base = super().__str__()
        return f"{base} [{self.note}]"

louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

def print_tree(tree, prefix=''):
    if tree == '-':
        print(prefix + '---')
        return
    name, father, mother = tree
    print(prefix + '--' + name)
    print_tree(father, prefix + '  |')
    print_tree(mother, prefix + '  |')

print_tree(margrethe_ii.ancestors())
