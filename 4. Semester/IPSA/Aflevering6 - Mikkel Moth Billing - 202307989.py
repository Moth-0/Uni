"""
HANDIN 6 - Ancestors

This handin is done by: 
    202307989 Mikkel Moth Billing 

Reflection upon solution: 
    I think the excersise went well, i used some time on the recursion part, but python tutor is the best. 
    For the subclass init i wanted to do something with **kwargs but i think that requires the the note is specified as 
    Person(note="note"), which it is not in Gerts example, I'm not sure if there is another way. 
    Overall i think the solution is good :)
"""

class Person:
    # Initialise Person
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died

    # Change string output
    def __str__(self):
        return f"{self.name} {self.born}-{self.died if self.died else ""}"
    
    # Get the parents with recursion
    def ancestors(self):
        return (str(self), 
                self.father.ancestors() if self.father else "-", 
                self.mother.ancestors() if self.mother else "-")
    
class AnnotatedPerson(Person):
    # Initialise Annotated with call to Person
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        self.note = note 
        Person.__init__(self, name, mother, father, born, died)

    # Add the note to the Person string 
    def __str__(self):
        return Person.__str__(self) + f" [{self.note}]"

# Tree Print from excersise 9.2
def print_tree(tree, pre=""):
    print(pre + "| -- " + tree[0]) 
    for child in tree[1:]:
        newpre = "|   " + pre 
        print_tree(child, newpre)

# Running example to see if it works       
louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

print_tree(margrethe_ii.ancestors())